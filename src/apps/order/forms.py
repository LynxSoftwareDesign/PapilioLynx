from django import forms
from apps.order.models import Pedido, Item, Estado, Material, Impresora

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

        labels = [
            'id_item' : 'Item',
            'id_pedido' : 'Pedido',
            'sys_impr' : 'Sistema de impresion',
            'tipo_material' : 'Tipo de Material',
            'impresion' : 'Impresion',
            'cantidad' : 'Cantidad',
            'observacion' : 'observacion',
        ]

        fields = [
            'id_item' : forms.TextInputs(),
            'id_pedido' : forms.TextInputs(),
            'sys_impr' : forms.Select(),
            'tipo_material' : forms.Select(),
            'impresion' : forms.Select(),
            'cantidad' : forms.TextInputs(),
            'observacion' : forms.TextInputs(),
        ]
