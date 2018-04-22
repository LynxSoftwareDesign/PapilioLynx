# Import Django
from django.contrib.auth.decorators import login_required
from django.urls import path, include

# Import interno
from apps.profiles.views import Index

urlpatterns = [
    path('', login_required(Index.as_view()), name = 'inicio'),

]
