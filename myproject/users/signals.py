from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver  #receiver is a decorator. It connects your custom function to a signal (like post_save), so it gets called when that signal is sent.
from .models import Profile

@receiver(post_save, sender=User) #When a User is saved, call this function. # sender = user >> This signal is listening to saves on the User model.
def create_profile(sender,instance,created,**kwargs):
    if created:                                    # created >> This is flag and is True only when a new user is created.
        Profile.objects.create(user=instance)     #If it's a new user, we create a Profile and link it to that user.

@receiver(post_save, sender=User)
def save_profile(sender,instance,**kwargs):
    instance.profile.save()   #ensures that any changes to User also trigger saving the related Profile.