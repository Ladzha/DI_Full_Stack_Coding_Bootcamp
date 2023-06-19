from django.contrib import admin
from django.urls import path
from .import views
from bookapp.views import *



urlpatterns = [
    path('', home, name='home'),
    path('add_review/', add_review, name ='add_review'),
    path('login/', views.LoginView.as_view(template_name = 'registration/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(template_name ='registration/register.html'), name='register'),
    path('profile/', user_profile,  name='profile'),


]
