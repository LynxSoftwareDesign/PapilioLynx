from django.urls import path, include
from apps.profiles.views import index, RegistroUsuario
from django.contrib.auth.views import login

urlpatterns = [
    path('', index, name = 'inicio'),
    path('registro', RegistroUsuario.as_view(), name = 'registro'),
    path('login',login, {'template_name':'board/forms/login.html'},name = 'login'),
]
