import json
import datetime
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import Message

class Consumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.user = self.scope['user']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        print(self.scope['user'].profile_picture)
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


    # Receive message from room group
    def chat_message(self, event):
        message = event['message']
        author = event['author']
        picture = event['picture']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message,
            'author' : author,
            'picture' : picture.split(r'/')[-1] 
        }))
