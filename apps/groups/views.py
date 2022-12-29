from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from users.models import User
from django.http import HttpResponse
from django.template import loader

def home(request):
    name  = request.path_info.split(r'/')[-1]
    mydata = '' 
    context = {'data': mydata}
    template = loader.get_template(r'tribe_page/home.html')

    if request.user.is_authenticated and (
            (not request.user.is_anonymous and request.user.tribe == request.path_info.split(r'/')[-1])
                 or request.user.is_superuser):


        return HttpResponse(template.render(context, request))

    else:
        template = loader.get_template(r'tribe_page/restricted.html')
        return HttpResponse(template.render(context, request))

