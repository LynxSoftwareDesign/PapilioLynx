# Import Django
from django.contrib.auth.decorators import login_required
from django.urls import path, include

# Import Interno
from apps.order.views import index, ItemsForm, OrderForm, OrderList

urlpatterns = [
    path('', index, name = 'inicio'),
    path('add_item', login_required(ItemsForm.as_view()), name = 'add_item'),
    path('pedidos', login_required(OrderList.as_view()), name = 'pedidos'),
    path('add_pedido', login_required(OrderForm.as_view()), name = 'add_pedido'),
]
