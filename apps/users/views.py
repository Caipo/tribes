from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.models import TribeUser
from django.http import HttpResponse
from django.template import loader

def profile(request):
    user = request.path_info.split(r'/')[-1]
    template = loader.get_template(r'profile.html')

    try:
        mydata = TribeUser.objects.get(username=user)
        context = {'exists' : True, 'user': mydata}
        return HttpResponse(template.render(context, request))

    except TribeUser.DoesNotExist:
        context = {'exists' : False} 
        return HttpResponse(template.render(context, request))

