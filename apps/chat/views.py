from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.template import loader
from chat.models import Message
from chat.consumer import get_clients

def room_name(request):
        if request.user.is_authenticated and (
                (not request.user.is_anonymous and request.user.tribe == request.path_info.split(r'/')[-3])
                     or request.user.is_superuser):
            name = request.path_info.split(r'/')[-3]
            messages = Message.objects.filter(tribe = request.user.tribe)

            print(get_clients()) 
            return render(request,
                          'chat.html', 
                         {'room_name': name,
                          'clients': get_clients(),
                          'user': request.user,
                          'past_messages' : messages
                         }
                          )

        else:
            template = loader.get_template(r'tribe_page/restricted.html')
            return HttpResponse(template.render(dict(), request))


