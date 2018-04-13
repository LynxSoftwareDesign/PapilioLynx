"""papilio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from papilio.views import inicio, clientes, contacto, nosotros, servicios
from apps.profiles.views import RegistroUsuario
from django.contrib.auth.views import login, logout_then_login

urlpatterns = [
    # Urls de Apps
    path('admin/', admin.site.urls),
    path('perfil/', include(('apps.profiles.urls', 'perfil'), namespace='perfil')),
    path('pedidos/', include(('apps.order.urls', 'pedidos'), namespace='pedidos')),

    #Urls internas
    path('', inicio, name = 'inicio'),
    path('inicio', inicio),
    path('clientes', clientes, name = 'clientes'),
    path('contacto', contacto, name = 'contacto'),
    path('nosotros', nosotros, name = 'nosotros'),
    path('servicios', servicios, name = 'servicios'),

    # Urls Gestion de Usuarios
    path('accounts/login/',login, {'template_name':'board/forms/login.html'},name = 'login'),
    path('accounts/register/', RegistroUsuario.as_view(), name = 'registro'),
    path('accounts/logout/', logout_then_login, name = 'logout'),

]
