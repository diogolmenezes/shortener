from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from encurtador.core.forms import ShortenerForm
from encurtador.core.models import Url
import json

def get(request, short):
  url = get_object_or_404(Url.objects, short=short)
  url.views += 1
  url.save()
  return HttpResponseRedirect(url.original)


def home(request):
  if request.method == 'POST':
    return create(request)
  else:
    return new(request)

def new(request):
  form = ShortenerForm()
  urls = Url.objects.all()
  return render(request, 'core/home/index.html', { 'form': form, 'urls': urls })

def create(request):
  form = ShortenerForm(request.POST)

  if form.is_valid():
    url   = Url.objects.filter(original=form.cleaned_data["url"])
    exist = url.count() > 0

    if exist:
      url = url[0]
    else:
      url = Url(original=form.cleaned_data["url"])
      url.save()

    to_json = { 'success': True, 'url': url.original, 'short': url.short }
  else:
    to_json = { 'success': False }

  return HttpResponse(json.dumps(to_json), content_type='application/json')

