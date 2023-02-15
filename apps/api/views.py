from django.shortcuts import render
from rest_framework.views import APIView
from chat.models import Message 
from accounts.models import TribeUser
from accounts.models import TribeUserSerializer
from rest_framework.response import Response
from .serializer import ReactSerializer



from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

class MessageView(APIView):
    serializer_class = ReactSerializer

    def get(self, request):
        messages = [{ 'sender' : i.sender.profile_picture, 'username' : i.sender.username ,'profile_picture' : i.sender.profile_picture, 'text': i.message, 'tribe': i.tribe }
                  for i in Message.objects.all()]
        return Response(messages)

class UsersView(APIView):
    serializer_class = TribeUserSerializer

    def get(self, request):
        users = [{'username' : i.username, 'profile_picture' : i.profile_picture } for i in TribeUser.objects.all()]
        return Response(users)

class LoginView(APIView):
#    serializer_class = ReactSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)    

    def post(self, request):
        data = request.POST.dict()
        username = data.get('username')
        password = data.get('password')

        # You can add your logic for authentication here

        # If authentication is successful, return a JSON response
        response = {
            'message': 'Login successful.'
        }
        return JsonResponse(response)
