# The User model here is the sender 

from django.db.models.signals import post_save
from django.contrib.auth.models import User 

# The receiver is going to get this signal from the User model when we have used the post_save signal is trigerred    
from django.dispatch import receiver 
from .models import Profile

@receiver(post_save, sender = User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)
    

@receiver(post_save, sender = User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()