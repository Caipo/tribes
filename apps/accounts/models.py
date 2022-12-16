from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class TribeUser(AbstractUser):
    tribe = models.CharField(max_length=30)
    profile_picture = models.URLField(max_length=200) 
    about = models.TextField(max_length=500)
    
@receiver(post_save, sender=TribeUser)
def my_handler(sender, instance, created, **kwargs):
    if created:
        instance.tribe = 'blap'

        instance.save()
    else:
        # Do something when an object is updated
        print("An object was updated!")

#not needed now but it will be
def find_tribe():
    pass

def get_proflie_picture():
    pass
