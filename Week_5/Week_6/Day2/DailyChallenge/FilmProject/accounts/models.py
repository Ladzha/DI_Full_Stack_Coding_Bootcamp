from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager

# from film.models import Film

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    # favorite_films  = models.ManyToManyField('Film')
    def __str__(self):
        return f'Profile: {self.user.username} {self.user.first_name} {self.user.last_name}'
    
    
class CustomUser(models.AbstractBaseUser):
    mood = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
