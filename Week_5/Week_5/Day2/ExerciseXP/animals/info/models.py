from django.db import models

# Create your models here.
class Animals(models.Model):
    #model - table
    name = models.CharField(max_length=20, default='cat')
    legs = models.IntegerField()
    weight = models.IntegerField()
    height = models.IntegerField()
    speed = models.IntegerField()
    family = models.ForeignKey('Family', on_delete=models.SET_NULL, null=True)

class Family(models.Model):
    name = models.CharField(max_length=20)