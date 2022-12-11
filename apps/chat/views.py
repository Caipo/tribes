from django.shortcuts import render

# letschat_app/views.py
from django.shortcuts import render
def app_index(request):
   return render(request, 'letschat_app/index.html')
