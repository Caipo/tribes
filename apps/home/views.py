from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def index(request):
    user = ''
    if request.user.is_authenticated:
            user = request.user

    template = loader.get_template('index.html')
    context = {'user' : user} 
    return HttpResponse(template.render(context, request))





