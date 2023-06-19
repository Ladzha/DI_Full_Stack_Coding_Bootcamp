from django import forms
from django.db import models
from .models import Person
from phonenumber_field.formfields import PhoneNumberField

from django.contrib import admin
from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget
from django.contrib.admin.widgets import AdminTextInputWidget

class SearchForm(forms.Form):
    number = PhoneNumberField(region='IL')
    # name = forms.CharField(required=False)

class SearchEmail(forms.Form):
    email = models.CharField()
    
    
class PersonAdminForm(forms.ModelForm):
    class Meta:
        model = Person
        widgets = {
            'phone_number': PhoneNumberInternationalFallbackWidget(),
        }