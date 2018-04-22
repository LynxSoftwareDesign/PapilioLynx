# Import Django
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

# Import interno
from apps.profiles.forms import RegistroForm
from apps.profiles.models import Profile

# Create your views here.
def index(request):
    return render(request, 'board/pages/inicio.html')

# Se crea l vista de Inicio
class Inicio(ListView):
    model = Profile
    template_name = 'board/pages/inicio.html'

    # Toma en cuenta el usuario logueado
    def get_queryset(self):
        return(Profile.objects.filter(cuenta=self.request.user))



# Registro de Usuarios
class RegistroUsuario(CreateView):
    model = User
    template_name = "board/forms/registro.html"
    form_class = RegistroForm
    success_url = reverse_lazy('perfil:inicio')
