from django.urls import path
from .views import *


urlpatterns = [
    path('homepage/', HomePageView.as_view(), name = 'homepage'),
    path('addFilm/', FilmCreateView.as_view(), name = 'addFilm'),
    path('addDirector/', DirectorCreateView.as_view(), name = 'addDirector'),
    path('addReview/', ReviewCreateView.as_view(), name = 'addReview'),
    path('deleteFilm/<int:pk>', FilmDeleteView.as_view(), name = 'deleteFilm'),
    path('favouriteFilm/<int:pk>', FavouriteFilmView.as_view(), name = 'favouriteFilm'),
    path('filmDetail/<int:pk>', FilmDetailView.as_view(), name = 'filmDetail'),

]