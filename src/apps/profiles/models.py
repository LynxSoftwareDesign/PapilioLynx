from django.db import models
from django.contrib import auth

# Perfil, Modelado de perfil en base de datos.
class Profile(models.Model):
    cuenta = models.ForeignKey(auth.user)
    direccion = models.TextField()
    telefono = models.CharField(max_length = 15)
    correo = models.EmailField()