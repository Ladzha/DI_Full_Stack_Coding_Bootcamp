from django.shortcuts import render, redirect
from django.db.models.signals import post_save
from .forms import ImageForm
from .models import NewImage, Profile
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from .forms import LoginForm, SignupForm 
from django.urls import reverse_lazy
from bookapp.forms import AddReviewForm

def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image =form.save()
            image.user = request.user
            image.save()
            return redirect('my-images')
    else:
        form = ImageForm()
    return render(request, 'image_share/upload_image.html', {'form': form})


# def upload_image(request):
#     if request.method == 'POST':
#         user = request.user
#         title = request.POST['title']
#         description = request.POST['description']
#         image_file = request.FILES['image_file']
#         NewImage.objects.create(user=user, title=title, description=description, image_file=image_file)
#         return redirect('my_images')
    
#     return render(request, 'image_share/upload_image.html')


def my_images(request):
    user = request.user
    all_my_img = NewImage.objects.filter(user=user)
    image_count = all_my_img.count()
    context = {'my_img_list': all_my_img, 'image_count':image_count}
    return render(request, 'image_share/my_images.html', context)

def all_images(request):
    all_img = NewImage.objects.all()
    context = {'img_list': all_img}
    return render(request, 'image_share/index.html', context)


@login_required
def user_profile(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    image_count = profile.image_count
    return render(request, 'registration/profile.html', {'user': user, 'profile': profile, 'image_count': image_count})

class LoginUserView(LoginView):
    form_class = LoginForm
    model = User
    template_name = 'login.html'
    success_url = reverse_lazy('all-images')

class LogoutUserView(LogoutView):
    template_name = 'index.html'
    success_url = reverse_lazy('all-images')
    
class RegisterView(CreateView):
    form_class = SignupForm
    model = User
    template_name = 'register.html'
    success_url = reverse_lazy('login')


