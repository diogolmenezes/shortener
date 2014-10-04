from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('encurtador.core.views',
    url(r'^$', 'home', name='home'),
    url(r'^(?P<short>[a-zA-Z0-9]{7})/$', 'get', name='get'),
)
