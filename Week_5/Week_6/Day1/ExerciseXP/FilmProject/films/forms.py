from django import forms
from .models import Film, Category, Country, Director

class FilmForm(forms.ModelForm):
    class Meta:
        instance = forms.ModelChoiceField()
        exclude = '__all__'
        
class DirectorForm(forms.ModelForm):
    class Meta:
        instance = forms.ModelChoiceField()
        exclude = '__all__'