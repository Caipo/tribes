from django.urls import path
from .views import room_name
from .views import app_index


urlpatterns = [
    #path('', app_index, name="index"),
    path('', room_name),
]
