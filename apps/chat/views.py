from django.shortcuts import render

from django.shortcuts import render
def app_index(request):
   return render(request, 'chat.html')

def room_name(request):
        name = request.path_info.split(r'/')[-3]
        print('asdf')
        return render(request, 'chat.html', {'room_name': name})

