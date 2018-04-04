from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return render(request, 'site/pages/inicio.html')

# Create your views here.
def clientes(request):
    return render(request, 'site/pages/clientes.html')

# Create your views here.
def contacto(request):
    return render(request, 'site/pages/contacto.html')

# Create your views here.
def nosotros(request):
    return render(request, 'site/pages/nosotros.html')

# Create your views here.
def servicios(request):
    return render(request, 'site/pages/servicios.html')
