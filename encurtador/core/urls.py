from django.conf.urls import patterns, include, url
from django.contrib import admin
from encurtador.core.views import Home, GoToUrl

urlpatterns = patterns('',
    url(r'^$', Home.as_view(), name='home'),
    url(r'^(?P<short>[a-zA-Z0-9]{7})/$', GoToUrl.as_view(), name='get'),
)
