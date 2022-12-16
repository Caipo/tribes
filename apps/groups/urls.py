from django.urls import re_path 
from .views import home 

urlpatterns = [
    re_path('^[a-z0-9_-]{3,15}$', home, name='home'),
]
