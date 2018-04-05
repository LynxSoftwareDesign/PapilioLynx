from django.urls import path, include
from apps.order.views import index, item

urlpatterns = [
    path('', index),
    path('item', item)
]
