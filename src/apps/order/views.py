from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from apps.order.models import Item
from apps.order.forms import ItemForm

# Create your views here.
def index(request):
    return HttpResponse('Pedidos')

# Se Crea Vista de Formulario Items
#def item_form(request):
#    if request.method == 'POST':    # Si recive un POST
#        form = ItemForm(request.POST)
#        if form.is_valid():     # Pregunto Si es Valido
#            form.save()         # Lo guardo
#        return redirect('perfil:inicio')
#    else:
#        form = ItemForm()

#    return render(request, 'board/forms/item.html', {'form':form})

#class ItemsLsit(ListView):
#    model = Item

class ItemsForm(CreateView):
    model = Item
    form_class = ItemForm
    template_name = 'board/forms/item.html'
    success_url = reverse_lazy('perfil:inicio')
