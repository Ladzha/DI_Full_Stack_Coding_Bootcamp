from django.shortcuts import render
from .models import Film, Category, Director, Country
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.urls import reverse_lazy
from .forms import FilmForm, DirectorForm
# Create your views here.

class HomePageView(ListView):
    model = Film
    template_name = 'homepage.html'
    context_object_name = 'homepage'
    
class FilmCreateView(CreateView):
    film_form = FilmForm
    template_name = 'addFilm.html'
    context_object_name = 'homepage'
    
class DirectorCreateView(CreateView):
    director_form = DirectorForm
    template_name = 'addDirector.html'
    context_object_name = 'homepage'