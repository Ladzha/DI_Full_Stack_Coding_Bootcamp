"""
URL configuration for img project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .import views
from image_share.views import upload_image, my_images, all_images, user_profile



urlpatterns = [
    path('', all_images, name ='all-images'),
    path('upload_image/', upload_image, name ='upload-image'),
    path('my_images/', my_images, name ='my-images'),
    path('login/', views.LoginView.as_view(template_name = 'registration/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(template_name ='registration/register.html'), name='register'),
    # path('profile/<int:id>', user_profile,  name='profile'),
    path('profile/', user_profile,  name='profile'),

]