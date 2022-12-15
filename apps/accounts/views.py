from django.shortcuts import render
from tribe_user.models import CustomUserCreationForm, CustomUser
from django.urls import reverse_lazy
from django.views import generic

def get_user_profile(request, username):
    user = CustomUser.objects.get(username=username)
    return render(request, 'registration/profile.html', {"user":user})

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
