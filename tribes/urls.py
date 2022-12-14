from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('user/', include('users.urls')),
    path('chat/', include('chat.urls')),
    path('', include('home.urls'))
]
