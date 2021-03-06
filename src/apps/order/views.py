# Import Django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

# Import interno
from apps.order.forms import ItemForm, PedidoForm
from apps.order.models import Item, Pedido

# Crea una vista en index
def index(request):
    return HttpResponse('Pedidos')

# Crea una instancia de Item
class ItemsForm(CreateView):
    model = Item
    form_class = ItemForm
    template_name = 'board/forms/add_item.html'
    success_url = reverse_lazy('perfil:inicio')


# Enlista los items de la Base de Datos
class ItemsList(ListView):
    model = Item
    template_name = 'board/forms/item.html'


# Crea una instancia de Item
class OrderForm(CreateView):
    model = Pedido
    form_class = PedidoForm
    template_name = 'board/forms/add_pedido.html'
    success_url = reverse_lazy('perfil:inicio')


# Enlista los items de la Base de Datos
class OrderList(ListView):
    model = Pedido
    template_name = 'board/pages/pedidos.html'
    paginate_by= 10

    # Toma en cuenta el usuario logueado
    def get_queryset(self):
        return(Pedido.objects.filter(cliente=self.request.user))
