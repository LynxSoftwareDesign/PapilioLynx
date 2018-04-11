from django import forms
from apps.order.models import  Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item

        fields = [
            'id_item',
            'id_pedido',
            'sys_impr',
            'tipo_material',
            'impresion',
            'cantidad',
            'observacion',
        ]

        labels = {
            'id_item' : 'idItem',
            'id_pedido' : 'idPedido',
            'sys_impr' : 'Sistema de Impresion',
            'tipo_material' : 'Tipo de Material',
            'impresion' : 'Impresion',
            'cantidad' : 'Cantidad',
            'observacion' : 'Detalles',
        }

        widgets = {
        'id_item' : forms.TextInput(),
        'id_pedido' : forms.TextInput(),
        'sys_impr' : forms.Select(),
        'tipo_material' : forms.Select(),
        'impresion' : forms.Select(),
        'cantidad': forms.TextInput(),
        'observacion' : forms.TextInput(),
        }
