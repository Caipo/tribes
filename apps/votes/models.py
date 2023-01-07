from django.db import models
from accounts.models import TribeUser

class Poll(model.Model):
    poll_type = model.CharField(max_length=100)
    tribe = model.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

class Vote(model.Model):
    user = models.ForeignKey(TribeUser, on_delete=models.CASCADE, related_name='vote_user')
    time_stamp = models.DatetimeField(aut_now_add=True)
    poll = model.ForeignKey(TribeUser, on_delete=models.CASCADE, related_name='poll')
    vote = models.CharField(max_lenght=100)
