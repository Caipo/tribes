from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tribe_user.models import CustomUser
from django.http import HttpResponse
from django.template import loader

def profile(request):
    user = request.path_info.split(r'/')[-1]
    template = loader.get_template(r'profile.html')

    mydata = CustomUser.objects.get(username=user)
    try:
        print(user)
        mydata = CustomUser.objects.get(username=user)
        context = {'exists' : True, 'user': mydata}
        return HttpResponse(template.render(context, request))

    except CustomUser.DoesNotExist:
        context = {'exists' : False} 
        return HttpResponse(template.render(context, request))
