from django.urls import path, include
from apps.profiles.views import index
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(index), name = 'inicio'),

]
