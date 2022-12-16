from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users.models import User
from django.http import HttpResponse
from django.template import loader

def home(request):
    name  = request.path_info.split(r'/')[-1]
    mydata = '' 
    context = {'data': mydata}
    template = loader.get_template(r'tribe_page/home.html')

    return HttpResponse(template.render(context, request))

