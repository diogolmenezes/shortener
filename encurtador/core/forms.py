from django import forms
from django.forms import ModelForm
from encurtador.core.models import Url

class UrlForm(ModelForm):
  class Meta:
    model  = Url
    fields = ['original']

