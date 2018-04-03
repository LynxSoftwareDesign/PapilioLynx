from django.urls import path, include
from apps.order.views import index

urlpatterns = [
    path(r'^$', index),
]
