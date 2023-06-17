from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class NewImage(models.Model):
    image = models.ImageField(upload_to='images')
    title = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'User: {self.user}, image: {self.title}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    image_count = models.IntegerField(default=0)
    

    def __str__(self):
            return f'Profile: {self.user.username}'
    
@receiver(post_save, sender=NewImage)
def update_image_count(sender, instance, created, **kwargs):
    if created:
        profile = Profile.objects.get(user=instance.user)
        profile.image_count = NewImage.objects.filter(user=instance.user).count()
        profile.save() 

    
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         profile=Profile.objects.create(user=instance)
#         profile.save() 


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
 
post_save.connect(create_profile, sender=User)
        
# def update_profile(sender, instance, created, **kwargs):
#     if created == False:
#         instance.profile.save()
# post_save.connect(update_profile, sender=User)

        