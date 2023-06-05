from django.shortcuts import render
from .models import Film, Category, Director, Country, Review
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.urls import reverse_lazy
from .forms import FilmForm, DirectorForm, ReviewForm
# Create your views here.

class HomePageView(ListView):
    model = Film # модель на которую ссылается. Будет отображаться список из этой модели. Т.е список фильмов или их параметров?
    template_name = 'homepage.html' #шаблон указывает, чтобы 
    context_object_name = 'homepage'
    
class FilmCreateView(CreateView):
    model = Film
    fields = '__all__'
    film_form = FilmForm
    template_name = 'film/addFilm.html'
    context_object_name = 'addFilm'
    success_url = reverse_lazy('addFilm')
    
class DirectorCreateView(CreateView):
    model = Director
    fields = '__all__'
    director_form = DirectorForm
    template_name = 'director/addDirector.html'
    context_object_name = 'addDirector'
    success_url = reverse_lazy('addDirector')
    
    
class ReviewCreateView(CreateView):
    model = Review
    director_form = ReviewForm
    fields = '__all__'
    template_name = 'review/addReview.html'
    context_object_name = 'addReview'
    success_url = reverse_lazy('addReview')