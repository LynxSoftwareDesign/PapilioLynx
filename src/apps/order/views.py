from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from apps.order.models import Item, Pedido
from apps.order.forms import ItemForm, PedidoForm

# Create your views here.
def index(request):
    return HttpResponse('Pedidos')

############################
#
# Crea una instancia de Item
# Actualizar modelado
#
###########################
class ItemsForm(CreateView):
    model = Item
    form_class = ItemForm
    template_name = 'board/forms/add_item.html'
    success_url = reverse_lazy('perfil:inicio')

############################
#
# Enlista los items de la Base de Datos
# Actualizar modelado
#
###########################
class ItemsList(ListView):
    model = Item
    template_name = 'board/forms/item.html'

############################
#
# Crea una instancia de Item
# Actualizar modelado
#
###########################
class OrderForm(CreateView):
    model = Pedido
    form_class = PedidoForm
    template_name = 'board/forms/item.html'
    success_url = reverse_lazy('perfil:inicio')


############################
#
# Enlista los items de la Base de Datos
# Actualizar modelado
#
###########################
class OrderList(ListView):
    model = Pedido
    template_name = 'board/forms/pedidos.html'
