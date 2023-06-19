from django import forms
from django.db import models
from .models import Person
from phonenumber_field.formfields import PhoneNumberField

class SearchForm(forms.Form):
    number = PhoneNumberField(region='IL')
    # name = forms.CharField(required=False)
