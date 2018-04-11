from django.urls import path, include
from apps.order.views import index

urlpatterns = [
    path('', index, name = 'inicio'),
    path('item', item, name = 'add_item')
]
