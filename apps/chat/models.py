from django.db import models
from accounts.models import TribeUser

class ConnectedUsers(models.Model):
    user  = models.ForeignKey(TribeUser,unique=True, on_delete=models.CASCADE, related_name='online_user')
    tribe = models.CharField(max_length=100)
    
class Message(models.Model):
     sender = models.ForeignKey(TribeUser, on_delete=models.CASCADE, related_name='sent_messages')
     message = models.TextField()
     tribe = models.CharField(max_length=100)
     profile_pic = models.CharField(max_length=100)
     timestamp = models.DateTimeField(auto_now_add=True)
