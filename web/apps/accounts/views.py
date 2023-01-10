from django.shortcuts import render
from .models import TribeUser 
from django.urls import reverse_lazy
from django.views import generic
from .forms import TribeUserCreationForm

def get_user_profile(request, username):
    user = TribeUser.objects.get(username=username)
    return render(request, 'registration/profile.html', {"user":user})


class SignUpView(generic.CreateView):
    form_class = TribeUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
