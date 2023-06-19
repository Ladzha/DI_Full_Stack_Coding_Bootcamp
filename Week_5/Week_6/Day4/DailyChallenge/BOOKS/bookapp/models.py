from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import requests


    
class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    published_date = models.DateField(blank=True)
    description = models.TextField()
    page_count = models.IntegerField(default=1)
    categories = models.CharField(max_length=250)
    thumbnail_url = models.URLField()


class BookReview(models.Model):
    associated_book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True, related_name='associated_book')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_profile')
    rating = models.IntegerField(default=0)
    review_text = models.TextField()
