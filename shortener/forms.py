from django import forms
from .models import ShortURL

class URLInputForm(forms.ModelForm):
    class Meta:
        model = ShortURL
        fields = ['url']