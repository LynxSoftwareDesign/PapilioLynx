# Import Django
from django.contrib.auth.decorators import login_required
from django.urls import path, include

# Import Interno
from apps.order.views import index, ItemsForm, OrderForm, OrderList

urlpatterns = [
    path('', index, name = 'inicio'),
    path('item', login_required(ItemsForm.as_view()), name = 'add_item'),
    path('pedidos', login_required(OrderList.as_view()), name = 'pedidos'),
]
