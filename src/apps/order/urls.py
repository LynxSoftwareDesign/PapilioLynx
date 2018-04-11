from django.urls import path, include
from apps.order.views import index, ItemsForm

urlpatterns = [
    path('', index, name = 'inicio'),
    path('item', ItemsForm.as_view(), name = 'add_item')
]
