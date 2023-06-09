from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from .forms import LoginForm, SignupForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class LoginUserView(LoginView):
    form_class = LoginForm
    model = User
    template_name = 'login.html'
    success_url = reverse_lazy('profile')

class LogoutUserView(LogoutView):
    template_name = 'homepage.html'
    success_url = reverse_lazy('login')
    
class RegisterView(CreateView):
    form_class = SignupForm
    model = User
    template_name = 'signup.html'
    success_url = reverse_lazy('homepage')


def user_profile(request, id):
    user = User.objects.get(id=id)
    return render(request, 'profile.html', {'user': user})
