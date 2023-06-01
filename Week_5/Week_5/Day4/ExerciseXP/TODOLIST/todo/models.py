from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField(null=True, blank=True)
    
    def __str__(self):
        return f'{self.name}'
    
class Todo(models.Model):
    title = models.CharField(max_length=20)
    details = models.CharField(max_length=20)
    has_been_done = models.BooleanField(default=False)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_completion  = models.DateTimeField(null=True, blank=True)
    deadline_date = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete = models.CASCADE, related_name='todos')
    def __str__(self):
        return f'{self.category} | {self.title}'