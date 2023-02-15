from django.urls import path
from .views import MessageView, UsersView, LoginView
from rest_framework.authtoken import views

urlpatterns = [
    path('message', MessageView.as_view(), name="index"),
    path('users', UsersView.as_view(), name="index"),
    path('login', LoginView.as_view(), name="index"),
    path('token', views.obtain_auth_token),
]

