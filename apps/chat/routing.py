from django.urls import path, include, re_path
from chat.consumer import Consumer
from .views import room_name

websocket_urlpatterns = [
    re_path(r"wss/(?P<room_name>\w+)/$", Consumer.as_asgi()),
]
