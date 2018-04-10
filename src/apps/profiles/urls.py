from django.urls import path, include
from apps.profiles.views import index

urlpatterns = [
    path('', index, name = 'inicio'),
]
