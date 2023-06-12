from django.db import models
from django.contrib.auth.models import User

OPTIONS_CHOICES = (
   ('SUN', 'sunny'),
   ('CL', 'cloudy'),
   ('WIN', 'windy'),
   ('RAI', 'rainy'),
   ('ST', 'stormy'),
)


# Create your models here.
class Report(models.Model):
    location= models.CharField(max_length=50)
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=5, choices=OPTIONS_CHOICES)
    forecaster = models.ForeignKey('Forecaster', on_delete=models.CASCADE)
    def __str__(self):
        return self.location
    
    
class Forecaster(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username