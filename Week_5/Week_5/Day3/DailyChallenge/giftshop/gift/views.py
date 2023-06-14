from django.shortcuts import render, redirect
from.models import Gif, Category
from .forms import CategoryForm, GifForm

# Create your views here.
def home(request):
    gifs_all = Gif.objects.all()
    context = {'gifs_list': gifs_all}
    return render(request, 'home.html', context)

def categories(request):
    categories_all = Category.objects.all()
    context = {'categories_list': categories_all}
    return render(request, 'categories.html', context)

def category(request, id):
    category = Category.objects.get(id=id)
    gifs_list = Gif.objects.filter(id=id)
    context = {'category': category, 'gifs_list': gifs_list}
    return render(request, 'category.html', context)

def gifs(request):
    gifs_all = Gif.objects.all()
    context = {'gifs_list': gifs_all}
    return render(request, 'gifs.html', context)

def gif(request, id):
    gif = Gif.objects.get(id=id)
    
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'like':
            gif.likes += 1
        elif action == 'dislike':
            gif.likes -= 1    
        gif.save()
     
    context = {'gif': gif}
    return render(request, 'gif.html', context)




def add_gif_view(request):
    #POST
    if request.method == 'POST':
        data = request.POST
        filled_form = GifForm(data)
        if filled_form.is_valid():
            filled_form.save()
            return redirect('home')

    # GET
    category_form = GifForm()
    context = {'form': category_form}
    return render(request, 'add_gif.html', context)

def add_category_view(request):
    
    if request.method == 'POST':
        data = request.POST
        filled_form = CategoryForm(data)
        if filled_form.is_valid():
            filled_form.save()
        return redirect('home')

    # GET
    category_form = CategoryForm()
    context = {'form': category_form}
    return render(request, 'add_category.html', context)

def like_gifs(request):
    popular_gifs = Gif.objects.filter(likes__gt=0).order_by('-likes')
    context = {'popular_gifs': popular_gifs}
    return render(request, 'like_gifs.html', context)
