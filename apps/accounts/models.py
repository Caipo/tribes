from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import random
import os


class TribeUser(AbstractUser):
    tribe = models.CharField(max_length=30)
    profile_picture = models.URLField(max_length=200) 
    about = models.TextField(max_length=500)
    banished = models.BooleanField(default=False)
    
@receiver(post_save, sender=TribeUser)
def my_handler(sender, instance, created, **kwargs):
    if created:
        instance.tribe = 'blap'
        instance.profile_picture = get_proflie_picture() 
        instance.save()
    else:
        # Do something when an object is updated
        print("An object was updated!")

#not needed now but it will be
def find_tribe():
    pass

def get_proflie_picture():
    directory = r'static/profile_pics/'
    files = os.listdir(directory)
    random_file = random.choice(files)
    random_image_path = os.path.join(directory, random_file)
    return random_image_path.replace('static','')
