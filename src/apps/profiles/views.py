from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from apps.profiles.forms import RegistroForm

# Create your views here.
def index(request):
    return render(request, 'board/pages/inicio.html')

class RegistroUsuario(CreateView):
    model = User
    template_name = "board/forms/registro.html"
    form_class = RegistroForm
    success_url = reverse_lazy('perfil:inicio')
