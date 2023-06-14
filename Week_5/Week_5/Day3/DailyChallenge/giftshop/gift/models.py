from django.db import models

# Create your models here.
class Gif(models.Model):
    likes = models.IntegerField(default=0)
    title = models.CharField(max_length=20)
    url = models.URLField()
    uploader_name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.title}'
    
class Category(models.Model):
    name = models.CharField(max_length=20)
    gifs = models.ManyToManyField('Gif', related_name='category')
    
    def __str__(self):
        return f'{self.name}'
