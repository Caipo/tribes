from django.shortcuts import render

from django.shortcuts import render
def app_index(request):
   return render(request, 'index.html')

def room_name(request, name):
        return render(request, 'chat.html', {'room_name': name})

def room(request, room_name):
  username = request.GET.get('username', 'Anonymous')

  return render(request, 'chat/room.html', {'room_name': room_name, 'username': username})
