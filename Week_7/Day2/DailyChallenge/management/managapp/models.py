from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    # admin = models.ForeignKey('DepartmentAdmin', on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name
    
class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number=models.CharField(max_length=20)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=None)
    project = models.ManyToManyField('Project') 
    
    def __str__(self) -> str:
        return self.name

    
class Task(models.Model):
    name = models.CharField(max_length=50)
    description=models.TextField()
    due_date=models.DateField()
    completed=models.BooleanField(default=False)
    project=models.ForeignKey('Project', on_delete=models.CASCADE, default=None, related_name='project')
    def __str__(self) -> str:
        return self.name
     
class Project(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField()
    start_date=models.DateField()
    end_date=models.DateField()
    def __str__(self) -> str:
        return self.name
    
class DepartmentAdmin(models.Model):
    admin = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username