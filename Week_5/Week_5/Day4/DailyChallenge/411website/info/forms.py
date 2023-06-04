from django import forms
from phonenumber_field.formfields import PhoneNumberField

class SearchForm(forms.ModelForm):
    class Meta:
        number = PhoneNumberField(region="IL")
        