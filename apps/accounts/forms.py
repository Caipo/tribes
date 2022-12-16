from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import TribeUser 

class TribeUserCreationForm(UserCreationForm):
    class Meta:
        model = TribeUser
        fields = ("username", "email")

class TribeUserChangeForm(UserChangeForm):
    class Meta:
        model = TribeUser
        fields = ("username", "email")
