from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users.models import User
from django.http import HttpResponse
from django.template import loader

def profile(request):
    user = request.path_info.split(r'/')[-1]

    try:
        mydata = User.objects.get(username=user)
        context = {'data': mydata}
        template = loader.get_template(r'users/profile.html')

        return HttpResponse(template.render(context, request))

    except User.DoesNotExist:
        template = loader.get_template(r'users/not_found.html')
        context = dict() 
        return HttpResponse(template.render(context, request))

