from django.urls import path
from .views import room_name


urlpatterns = [
    path('', room_name),
]
