from django.contrib.auth.models import User
from django.db import models

# Se modela Tipos de Cuentas
class TipoCuenta(models.Model):
    nombreTipo = models.CharField(max_length = 25)
    adm_menu = models.BooleanField()

# Modelado de perfil.
class Profile(models.Model):
    cuenta = models.OneToOneField(User, on_delete=models.CASCADE)   # Se enlaza uno a uno con los usuarios
    tipo_cuenta = models.OneToOneField(TipoCuenta, on_delete=models.CASCADE, null=True, blank=True)
    direccion = models.CharField(max_length = 50, null=True, blank=True)
    telefono = models.CharField(max_length = 15, null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
