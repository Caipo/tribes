from django.shortcuts import render

from django.shortcuts import render
def app_index(request):
   return render(request, 'index.html')

def room_name(request, name):
        return render(request, 'chat.html', {'room_name': name})

