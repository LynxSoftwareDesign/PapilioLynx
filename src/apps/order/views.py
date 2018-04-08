from django.shortcuts import render, redirect
from django.http import HttpResponse
#from apps.order.forms import ItemForm

# Create your views here.
def index(request):
    return HttpResponse('Pedidos')

# Se Crea Vista de Formulario Items
#def item(request):
#    if request.method == 'POST':    # Si recive un POST
#        form = ItemForm(request.POST)
#        if form.is_valid():     # Pregunto Si es Valido
#            form.save()     # Lo guardo
#        return redirect('')
#    else:
#        form = ItemForm

#S    return render(request, 'board/forms/item.html', {'form':form})
