from django.db import models

# Se crea modelo para los estados
class Estado(models.Model):
    id_estado = models.IntegerField(primary_key=True)
    nombre_estado = models.CharField(max_length=30)

# Se crea modelo de pedidos
class Pedido (models.Model):
    # idCliente
    # idPedido
    # idItem
    estado = models.ForeignKey(Estado, null=False, blank=False, on_delete=models.CASCADE) #Clae foranea de Estados

