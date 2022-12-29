# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import TribeUserCreationForm, TribeUserChangeForm
from .models import TribeUser

class TribeUserAdmin(UserAdmin):
    add_form = TribeUserCreationForm
    form = TribeUserChangeForm
    model = TribeUser
    list_display = ["email", "username",]

admin.site.register(TribeUser, TribeUserAdmin)
