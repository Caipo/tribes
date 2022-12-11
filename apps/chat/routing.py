from django.urls import path, include
from chat.consumer import Consumer

websocket_urlpatterns = [
  path('ws//', Consumer.as_asgi()), # Using asgi
]
