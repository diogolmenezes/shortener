from django import forms

class ShortenerForm(forms.Form):
  url = forms.CharField(max_length=200)

