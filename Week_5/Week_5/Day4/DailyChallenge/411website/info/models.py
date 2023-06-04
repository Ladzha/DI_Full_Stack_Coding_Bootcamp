from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(unique=True)
    phone_number = PhoneNumberField(region='IL')
    address = models.CharField(max_length=100)
    
    
    def __str__(self) -> str:
        return self.name
