from django.shortcuts import render, redirect
from .models import Film, Category, Director, Country, Review
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic import ListView, View
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
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
    


class FilmDeleteView(UserPassesTestMixin, DeleteView): #...
    model = Film
    template_name = 'film/confirm_delete.html'
    context_object_name = 'post'
    success_url = reverse_lazy('homepage')
    
    def test_func(self): 
        if self.request.user.is_superuser:
            return True
        else:
            return False 
    
# User = get_user_model()

# class FavouriteFilmView(View):
#     def post(self, request, **kwargs):
#         user = self.request.user
#         user.favorite_films.all()
#         film_id = kwargs['film_id']
#         film = get_object_or_404(Film, id=film_id)

#         if film in user.favorite_films.all():
#             user.favorite_films.remove(film)
#         else:
#             user.favorite_films.add(film)
#             messages.success(request, "Film added to favorites.")

#         return ('homepage') 
    

class FavouriteFilmView(View):
   
    def post(self,request, film_id): 
        
        film = get_object_or_404(Film, id=film_id)
        user = self.request.user
        user_profile = user.user_profile
        print(user_profile)

        if film in user_profile.favorite_film.all():
            user_profile.favorite_film.remove(film)
            messages.success(request, "Film removed from favorites.")
        else:
            user_profile.favorite_film.add(film)
            messages.success(request, "Film added to favorites.")
            
        return redirect('homepage')


class FilmDetailView(DetailView):
    model = Film
    template_name = 'film/filmDetail.html'
    context_object_name = 'filmDetail'
    
