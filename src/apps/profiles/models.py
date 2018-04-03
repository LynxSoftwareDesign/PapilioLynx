from django.db import models
from django.contrib.auth.models import User

# Perfil, Modelado de perfil en base de datos.
class Profile(models.Model):
    cuenta = models.OneToOneField(User, on_delete=models.CASCADE)   # Se enlaza uno a uno con los usuarios
    direccion = models.TextField()
    telefono = models.CharField(max_length = 15)
    correo = models.EmailField()
    id_cliente = models.IntegerField()
    fecha_nacimiento = models.DateField(null=True, blank=True)
