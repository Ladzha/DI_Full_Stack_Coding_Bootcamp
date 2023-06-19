from django.urls import path
from .views import *


urlpatterns = [
    path('homepage/', HomePageView.as_view(), name = 'homepage'),
    path('addFilm/', FilmCreateView.as_view(), name = 'addFilm'),
    path('addDirector/', DirectorCreateView.as_view(), name = 'addDirector'),
    path('addReview/', ReviewCreateView.as_view(), name = 'addReview'),
    path('deleteFilm/<int:id>', FilmDeleteView.as_view(), name = 'deleteFilm'),

]
