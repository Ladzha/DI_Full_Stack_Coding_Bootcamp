from django import forms
from .models import Todo, Category

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title', 'details', 'deadline_date', 'category')
        widgets = {
            'deadline_date': forms.DateInput(attrs={'type': 'date'})
        }
        
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        # fields = (title, details, dedline_date, category)
        # exclude = ['created_at']
        fields = '__all__'
        
class DoneForm(forms.ModelForm):
    class Meta:
        instance = forms.ModelChoiceField()
        # fields = ('title', 'details', 'deadline_date', 'category')
        exclude = '__all__'
    