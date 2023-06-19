from django.db import models

# Create your models here.

class Customer (models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(unique=True)
    phone_number=models.IntegerField()
    address=models.CharField(max_length=250)
    city=models.CharField(max_length=250)
    country=models.CharField(max_length=250)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'  

class Vehicle(models.Model):
    vehicle_type =models.ForeignKey('VehicleType', on_delete=models.CASCADE) #(foreign key to Vehicle Type model)
    date_created=models.DateTimeField(auto_now_add=True)
    real_cost = models.IntegerField()   #(how much it costs)
    size = models.ForeignKey('VehicleSize', on_delete=models.CASCADE) #(foreign key to Vehicle Size model)
    
    def __str__(self):
        return f'{str(self.vehicle_type)} {str(self.size)}'


class VehicleType(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class VehicleSize(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
class Rental(models.Model):
    rental_date= models.DateField(null=True)
    return_date= models.DateTimeField(null=True, blank=True)
    customer= models.ForeignKey('Customer', on_delete=models.CASCADE)  #(foreign key to Customer)
    vehicle= models.ForeignKey('Vehicle', on_delete=models.CASCADE) #(foreign key to Vehicle)
    
    def __str__(self):
        return f'{str(self.customer)} / {str(self.vehicle)}'

class RentalRate(models.Model):
    daily_rate=models.IntegerField()
    vehicle_type=models.ForeignKey('VehicleType', on_delete=models.CASCADE) #(foreign key to Vehicle Type)
    vehicle_size=models.ForeignKey('VehicleSize', on_delete=models.CASCADE) #(foreign key to Vehicle Size)
    def __str__(self):
        return str(self.vehicle_type)

class RentalStation(models.Model):
    name=models.CharField(max_length=250)
    capacity=models.PositiveIntegerField(default=0) #(amount of vehicles it can store)
    address=models.ForeignKey('Address', on_delete=models.CASCADE) #(foreign key to Address)
    def __str__(self):
        return self.name

class Address(models.Model):
    address= models.CharField(max_length=250, default= None)
    address2=models.CharField(max_length=250, blank = True, default= None)
    city=models.CharField(max_length=250, default= None)
    country=models.CharField(max_length=250, default= None)
    postal_code=models.IntegerField(default= None)
    def __str__(self):
        return self.address