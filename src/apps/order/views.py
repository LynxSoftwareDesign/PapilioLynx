from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from apps.order.forms import ItemForm

# Create your views here.
def index(request):
    return HttpResponse('Pedidos')

# Se Crea Vista de Formulario Items
def item(request):
    if request.method == 'POST':    # Si recive un POST
        form = ItemForm(request.POST)
        if form.is_valid():     # Pregunto Si es Valido
            product = form.save()
            product.save()      # Lo guardo
        return redirect('')
    else:
        form = ItemForm

    template = loader.get_template('board/forms/item.html')
    context = {'form':form}

    #return render(request, 'board/forms/item.html', {'form':form})
    return HttpResponse(template.render(context, request))
