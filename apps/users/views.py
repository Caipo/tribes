from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users.models import User
from django.http import HttpResponse
from django.template import loader

def profile(request):
    user = request.path_info.split(r'/')[-1]
    template = loader.get_template(r'profile.html')
    print(user)

    try:
        mydata = User.objects.get(username=user)
        print(mydata)
        context = {'exists' : True, 'user': mydata}
        return HttpResponse(template.render(context, request))

    except User.DoesNotExist:
        context = {'exists' : False} 
        return HttpResponse(template.render(context, request))

