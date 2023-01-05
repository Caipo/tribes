from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.template import loader
from chat.models import Message
from chat.models import ConnectedUsers 

def room_name(request):
        if request.user.is_authenticated and (
                (not request.user.is_anonymous and request.user.tribe == request.path_info.split(r'/')[-3])
                     or request.user.is_superuser):
            name = request.path_info.split(r'/')[-3]
            messages = Message.objects.filter(tribe = request.user.tribe)
            user_list =  [i.user for i in ConnectedUsers.objects.filter(tribe = request.user.tribe)]

            
            return render(request,
                          'chat.html', 
                         {'room_name': name,
                          'user': request.user,
                          'user_list' : user_list,
                          'past_messages' : messages
                         }
                        )

        else:
            template = loader.get_template(r'tribe_page/restricted.html')
            return HttpResponse(template.render(dict(), request))
