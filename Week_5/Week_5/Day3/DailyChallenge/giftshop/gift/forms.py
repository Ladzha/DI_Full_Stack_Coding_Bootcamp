from django import forms
from .models import Category, Gif
# from .forms import CategoryForm, GifForm

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        
class GifForm(forms.ModelForm):
    class Meta:
        model = Gif
        fields = '__all__'
        exclude = ['created_at', 'likes']