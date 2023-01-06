from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from accounts.models import TribeUser
from django.http import HttpResponse
from django.template import loader

def home(request):
    name  = request.path_info.split(r'/')[-1]
    
    context = {}
    template = loader.get_template(r'tribe_page/home.html')

    if request.user.is_authenticated and (
       (not request.user.is_anonymous 
          and request.user.tribe == request.path_info.split(r'/')[-1])
            or request.user.is_superuser):

        users = TribeUser.objects.filter(tribe = request.user.tribe)
        context = {'user_list' : users}

        return HttpResponse(template.render(context, request))

    else:
        template = loader.get_template(r'tribe_page/restricted.html')
        return HttpResponse(template.render(context, request))

