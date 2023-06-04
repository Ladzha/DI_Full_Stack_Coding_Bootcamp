from django import forms
from .models import Todo, Category

class TodoForm(forms.ModelForm):
    # field_name = forms.ChoiceField(**options)
    class Meta:
        model = Todo
        fields = ('title', 'details', 'deadline_date', 'category', 'has_been_done')
        widgets = {
            'deadline_date': forms.DateInput(attrs={'type': 'date'})
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class DoneForm(forms.ModelForm):
    class Meta:
        # instance = forms.ModelChoiceField()
        fields = ('title', 'details', 'deadline_date', 'category')
    