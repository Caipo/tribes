from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import random
import os
from rest_framework import serializers
import django.contrib.auth.models as django_auth_models

#from django.conf import settings
#from django.dispatch import receiver
#from django.db.models.signals import post_save
#from rest_framework.authtoken.models import Token

class TribeUser(AbstractUser):
    tribe = models.CharField(max_length=30)
    profile_picture = models.URLField(max_length=200) 
    about = models.TextField(max_length=500)
    banished = models.BooleanField()


class TribeUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TribeUser
        fields = ('id', 'username', 'tribe', 'profile_picture', 'about', 'banished')


@receiver(post_save, sender=TribeUser)
def my_handler(sender, instance, created, **kwargs):
    if created:
        instance.tribe = 'blap'
        instance.profile_picture = get_proflie_picture() 
        instance.save()
    else:
        # Do something when an object is updated
        print("An object was updated!")


#@receiver(post_save, sender=settings.AUTH_USER_MODEL)
#def create_auth_token(sender, instance=None, created=False, **kwargs):
#    if created:
#        Token.objects.create(user=instance)

def get_proflie_picture():
    directory = r'static/profile_pics/'
    files = os.listdir(directory)
    random_file = random.choice(files)
    random_image_path = os.path.join(directory, random_file)
    return random_image_path.replace('static','')

django_auth_models.AnonymousUser = TribeUser
