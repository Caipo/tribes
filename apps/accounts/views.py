from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

def get_user_profile(request, username):
    user = User.objects.get(username=username)
    return render(request, 'registration/profile.html', {"user":user})

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
