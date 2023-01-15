from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TribeUser 
from django.urls import reverse_lazy
from django.views import generic
from .forms import TribeUserCreationForm
from django.contrib.auth import authenticate, login

def get_user_profile(request, username):
    user = TribeUser.objects.get(username=username)
    return render(request, 'registration/profile.html', {"user":user})


class SignUpView(generic.CreateView):
    form_class = TribeUserCreationForm
    success_url = '/'
    template_name = "registration/signup.html"

    def form_valid(self, form):
        #save the new user first
        form.save()
        #get the username and password
        username = self.request.POST['username']
        password = self.request.POST['password1']
        #authenticate user then login
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return HttpResponseRedirect(self.success_url)
