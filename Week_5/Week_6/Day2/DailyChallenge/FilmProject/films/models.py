from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return f'{self.name}'
    
class Category(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return f'{self.name}'
    
class Director(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Film(models.Model):
    title = models.CharField(max_length=20)
    release_date = models.DateField(auto_now_add=True)
    created_in_country = models.ForeignKey('Country', on_delete=models.SET_NULL, null=True, related_name='created_country')
    available_in_countries = models.ManyToManyField('Country')
    category = models.ManyToManyField('Category')
    director  = models.ManyToManyField('Director')
    
    

    def __str__(self):
        return f'{self.title}'
    
class Review(models.Model):
    film = models.ForeignKey('Film', on_delete=models.SET_NULL, null=True, related_name='reviews')
    review_text = models.TextField()
    rating = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    review_date = models.DateTimeField(auto_now_add=True)
    review_author = models.ForeignKey('CustomUser', on_delete=models.SET_NULL, null=True, related_name='author')

    def __str__(self):
        return f'{self.film}'

