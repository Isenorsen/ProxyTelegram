from django import forms
from django.forms import ModelForm
from django.db import models
from .models import Proxy

class ContactForm(forms.Form):
    period = forms.CharField(max_length=100)
    nickname = forms.CharField(max_length=100)
    email = forms.EmailField()

class AddingProxyForm(ModelForm):
    class Meta:
        model = Proxy
        fields = ['channel_name', 'nickname', 'description', 'url', 'avatar', 'active', 'button_url']
