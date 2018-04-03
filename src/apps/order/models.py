from django.db import models
from django.contrib.auth.models import User

# Se crea modelo para los estados
class Estado(models.Model):
    id_estado = models.IntegerField(primary_key=True)
    nombre_estado = models.CharField(max_length=30)

# Se crea modelo de pedidos
class Pedido(models.Model):
    id_cliente = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    id_pedido = models.IntegerField(primary_key=True)
    estado = models.ForeignKey(Estado, null=False, blank=False, on_delete=models.CASCADE) #Clave foranea de Estados

#Se crea modelo de materiales para impresion
class Material(models.Model):
    id_mat = models.IntegerField(primary_key=True)
    id_imp = ForeignKey(Impresora, null=False, blank=False, on_delete=models.CASCADE)
    nombre_mat = models.CharField(max_length=50)

#Se modela las impresoras
class Impresora(models.Model):
    id_imp = models.IntegerField(primary_key=True)
    nombre_imp = models.CharField(max_length=50)

# Se crea mdoelo para Items
class Item(models.Model):
    id_item = models.IntegerField(primary_key=True)
    id_pedido = models.ForeignKey(Pedido, blank=False, on_delete=models.CASCADE)
    sys_impr = ForeignKey(Impresora, null=False, blank=False, on_delete=models.CASCADE)
    tipo_material = ForeignKey(Material, null=True, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    observacion = models.models.TextField()
