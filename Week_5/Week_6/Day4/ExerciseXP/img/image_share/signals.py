from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import NewImage, Profile

@receiver(post_save, sender=NewImage)
def update_image_count(sender, instance, created, **kwargs):
    if created:
        profile = Profile.objects.get(user=instance.user)
        profile.image_count = NewImage.objects.filter(user=instance.user).count()
        profile.save()