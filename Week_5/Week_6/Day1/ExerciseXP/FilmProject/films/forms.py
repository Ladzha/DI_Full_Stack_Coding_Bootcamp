from django import forms
from .models import Film, Category, Country, Director

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        exclude = '__all__'
        
class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        exclude = '__all__'      
