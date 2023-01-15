import json
import datetime
import bleach
import re
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import Message

clients = list()

class Consumer(WebsocketConsumer):
    def connect(self):
        clients.append(self)
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.user = self.scope['user']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name,
        )


        # Keeps track of online users
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'user_list',
            }
        )

        self.accept()

    def disconnect(self, close_code):
        clients.remove(self)

        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'user_list',
            }
        )


        

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        chat_message = Message(sender=self.scope['user'], 
                                   profile_pic = self.scope['user'].profile_picture.split('/')[-1],
                                   tribe = self.scope['user'].tribe,
                                   message=message)
        chat_message.save()
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'author': self.scope['user'].username,
                'picture' : self.scope['user'].profile_picture,
                'time' :  str(datetime.datetime.now())
            }
        )

    
    def user_list(self, event):
        self.send(text_data=json.dumps({
            'type' : 'user_list',
            'clients' : get_clients(),
        }))

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']
        author = event['author']
        picture = event['picture']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'type' : 'chat_message',
            'message': filter_message(message),
            'author' : author,
            'picture' : picture.split(r'/')[-1] 
        }))

def filter_message(message):
    allowed_tags = ['a', 'b','br', 'em', 'i', 'strong']
    allowed_attributes = {}
    
    img_re = '^https?://.+\.(png|jpg|jpeg|gif|bmp)$'
    if re.match(img_re, message):
        return f'<img src="{message}"  width="400">'

    return bleach.clean(message, tags=allowed_tags, attributes=allowed_attributes)

def get_clients():
    return [ {'username' : i.user.username, 'profile_picture' : i.user.profile_picture } for i in sorted(set(clients), key = lambda x: x.user.username )]
