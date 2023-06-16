from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from image_share.models import NewImage

class ImageForm(forms.ModelForm):
    class Meta:
        model = NewImage
        fields = ['image', 'title', 'description', 'user']
        
class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']

class LoginForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
