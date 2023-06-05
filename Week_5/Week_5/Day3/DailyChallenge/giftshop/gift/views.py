from django.shortcuts import render
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
    context = {'gif': gif}
    return render(request, 'gif.html', context)

def add_gif_view(request):
    
    if request.method == 'POST':
        data = request.POST
        filled_form = GifForm(data)
        filled_form.save()

    # GET
    category_form = GifForm()
    context = {'form': category_form}
    return render(request, 'add_gif.html', context)

def add_category_view(request):
    
    if request.method == 'POST':
        data = request.POST
        filled_form = CategoryForm(data)
        filled_form.save()

    # GET
    category_form = CategoryForm()
    context = {'form': category_form}
    return render(request, 'add_category.html', context)

def like_gifs(request, id):
    gifs_all = Gif.objects.filter(id=id) #change for likes
    context = {'gifs_list': gifs_all}
    return render(request, 'gifs.html', context)