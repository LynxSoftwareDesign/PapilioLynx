from django.db import models
from django.contrib.auth.models import User

# Se crea modelo para los estados
class Estado(models.Model):
    nombre_estado = models.CharField(max_length=30)
    color_estado = models.CharField(max_length=30)

    def __str__(self):
        return '{}'.format(self.nombre_estado)

# Se crea modelo de pedidos
class Pedido(models.Model):
    cliente = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado, null=False, blank=False, on_delete=models.CASCADE) #Clave foranea de Estados

#Se modela las impresoras
class Impresora(models.Model):
    nombre_imp = models.CharField(max_length=50)

    #Retorna el nombre
    def __str__(self):
        return '{}'.format(self.nombre_imp)

#Se crea modelo de materiales para impresion
class Material(models.Model):
    nombre_mat = models.CharField(max_length=50)

    #Retorna el nombre
    def __str__(self):
        return '{}'.format(self.nombre_mat)

# Se crea mdoelo para Items
class Item(models.Model):
    pedido = models.ForeignKey(Pedido, blank=False, on_delete=models.CASCADE)
    sys_impr = models.ForeignKey(Impresora, null=False, blank=False, on_delete=models.CASCADE)
    tipo_material = models.ForeignKey(Material, null=True, on_delete=models.CASCADE)   # Tipo de lienzo depende de la impresora
    impresion = models.CharField(max_length=50) # Simple o Doble Faz (Puede ser nulo)
    cantidad = models.IntegerField()
    nombre_item = models.CharField(max_length=50)
    observacion = models.TextField()

    #Retorna el nombre
    def __str__(self):
        return '{}'.format(self.nombre_item)
