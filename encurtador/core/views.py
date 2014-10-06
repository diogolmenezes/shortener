from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, View
from encurtador.core.forms import UrlForm
from encurtador.core.models import Url
import json

class Home(CreateView):
  form_class    = UrlForm
  model         = Url
  template_name = 'core/home/index.html'

  def get_context_data(self, **kwargs):
    context = super(Home, self).get_context_data(**kwargs)
    context['urls'] = Url.objects.all()[:5]
    return context

  def form_invalid(self, form):
    to_json = { 'success': False }
    return HttpResponse(json.dumps(to_json), content_type='application/json')

  def form_valid(self, form):
    url   = Url.objects.filter(original=form.cleaned_data["original"])
    exist = url.count() > 0

    if exist:
      url = url[0]
    else:
      url = form.save()

    to_json = { 'success': True, 'original': url.original, 'short': url.short }

    return  HttpResponse(json.dumps(to_json), content_type='application/json')

class GoToUrl(View):
  def get(self, *args, **kwargs):
    url = get_object_or_404(Url.objects, short=kwargs['short'])
    url.views += 1
    url.save()
    return HttpResponseRedirect(url.original)

