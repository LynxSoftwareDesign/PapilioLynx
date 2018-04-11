from django.contrib import admin
from apps.order.models import Estado, Pedido, Impresora, Material, Item

# Register your models here.
admin.site.register(Estado)
admin.site.register(Pedido)
admin.site.register(Impresora)
admin.site.register(Material)
admin.site.register(Item)
