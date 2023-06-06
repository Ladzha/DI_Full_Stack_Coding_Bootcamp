from django.shortcuts import render
from .models import Film, Category, Director, Country, Review
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.urls import reverse_lazy
from .forms import FilmForm, DirectorForm, ReviewForm
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        UserPassesTestMixin,
                                        PermissionRequiredMixin)
# Create your views here.

class HomePageView(ListView):
    model = Film
    template_name = 'homepage.html'
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
    
    
class FilmUpdateView(UserPassesTestMixin, UpdateView):

    def test_func(self): 
        #<-----function that returns True/False when user tries to reach the view
        if self.user.is_superuser:
            return True
        else:
            return False 
        #<-----Leads to a 403 (forbidden) page
    
class FilmDeleteView(DeleteView):
    pass #
    # model = Film
    # fields = '__all__'
    # film_form = FilmForm
    # template_name = 'film/addFilm.html'
    # context_object_name = 'addFilm'
    # success_url = reverse_lazy('addFilm')
    
    # Create a new class-based view, FilmDeleteView, in the films app that inherits from generic.DeleteView. This view should handle the deletion of a film object. Override the get_queryset method to restrict access to this view to superusers