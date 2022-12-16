# accounts/urls.py
from django.urls import path, re_path
from .views import SignUpView 

urlpatterns = [
    path(r'signup/', SignUpView.as_view(), name="signup"),
]
