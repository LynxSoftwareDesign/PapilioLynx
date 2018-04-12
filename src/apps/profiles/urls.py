from django.urls import path, include
from apps.profiles.views import index, RegistroUsuario

urlpatterns = [
    path('', index, name = 'inicio'),
    path('registro', RegistroUsuario.as_view(), name = 'registro'),
]
