from django.test import TestCase
from django.core.urlresolvers import reverse
from encurtador.core.shorter  import to_short
from encurtador.core.models  import Url

class TestEncurtador(TestCase):

  def test_deve_encurtar(self):
    url = to_short('http://google.com.br')
    self.assertEqual(url, 'cf5f259')

  def test_deve_encurtar_igual_mesma_url(self):
    url  = to_short('http://google.com.br')
    url2 = to_short('http://google.com.br')
    self.assertEqual(url, url2)

  def test_deve_encurtar_diferente_urls_diferentes(self):
    url  = to_short('http://google.com.br')
    url2 = to_short('http://google.com')
    self.assertNotEqual(url, url2)

class TestHomeView(TestCase):
  def test_home_must_have_5_most_viewed_urls(self):
    top_5 = [x.original for x in Url.objects.all()[:5]]
    response = self.client.get(reverse("core:home"))
    for url in top_5:
      self.assertContains(response.content, url)

class TestUrlModel(TestCase):
  def setUp(self):
    self.url = Url(original='http://google.com.br')

  def test_has_0_views_on_save(self):
    self.url.save()
    self.assertEqual(self.url.views, 0)


class TestRecoverUrl(TestCase):

  def setUp(self):
    self.url = Url(original='http://google.com.br')
    self.url.save()

  def test_must_add_1_view_on_render(self):
    response = self.client.get(reverse("core:get", kwargs={'short': self.url.short}))
    self.assertRedirects(response, self.url.original, status_code=302, target_status_code=200, msg_prefix='')

  def test_must_redirect_to_original_url(self):
    response = self.client.get(reverse("core:get", kwargs={'short': '1234567'}))
    self.assertEqual(response.status_code, 404)

  def test_must_404_when_short_url_does_not_exist(self):
    response = self.client.get(reverse("core:get", kwargs={'short': '1234567'}))
    self.assertEqual(response.status_code, 404)





