from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from films.models import Film

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    favorite_film = models.ManyToManyField(Film, related_name='users_favorite', blank=True)

    def __str__(self):
        return f'Profile: {self.user.username} {self.user.first_name} {self.user.last_name}'

class User(AbstractUser):
    favorite_films = models.ManyToManyField(Film, related_name='users_favorite', blank=True)
    groups = models.ManyToManyField(Group, related_name='accounts_users', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='accounts_users', blank=True)
    def __str__(self):
        return f'Profile: {self.user.username}' 