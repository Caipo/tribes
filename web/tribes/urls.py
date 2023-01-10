from django.contrib import admin
from django.urls import path, include, re_path


from .views import FrontendAppView, test

urlpatterns = [
    path('', FrontendAppView.as_view()),
    path('api/test/', test),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('u/', include('users.urls')),
    path('t/', include('groups.urls')),
    re_path(r't/[a-z0-9_-]{3,15}/chat/', include('chat.urls')),
    path('', include('home.urls'))
]
