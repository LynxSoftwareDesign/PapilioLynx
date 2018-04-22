from django.contrib.auth.models import User
from django.db import models

# Perfil, Modelado de perfil en base de datos.
class Profile(models.Model):
    cuenta = models.OneToOneField(User, on_delete=models.CASCADE)   # Se enlaza uno a uno con los usuarios
    direccion = models.TextField(null=True, blank=True)
    telefono = models.CharField(max_length = 15, null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
