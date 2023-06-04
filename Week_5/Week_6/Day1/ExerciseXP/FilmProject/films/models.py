from django.db import models


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
    

