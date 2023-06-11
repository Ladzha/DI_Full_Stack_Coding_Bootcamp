from django.db import models

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
    def __str__(self):
        return self.location