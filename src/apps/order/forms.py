from django import forms
from apps.order.models import  Item, Pedido

# Creacion de Items
class ItemForm(forms.ModelForm):
    class Meta:
        model = Item

        fields = [
            'pedido',
            'sys_impr',
            'tipo_material',
            'impresion',
            'cantidad',
            'observacion',
        ]

        labels = {
            'pedido' : 'pedido',
            'sys_impr' : 'Sistema de Impresion',
            'tipo_material' : 'Tipo de Material',
            'impresion' : 'Impresion',
            'cantidad' : 'Cantidad',
            'observacion' : 'Detalles',
        }

        widgets = {
        'pedido' : forms.TextInput(attrs={'class':'form-control'}),
        'sys_impr' : forms.Select(attrs={'class':'form-control'}),
        'tipo_material' : forms.Select(attrs={'class':'form-control'}),
        'impresion' : forms.Select(attrs={'class':'form-control'}),
        'cantidad': forms.TextInput(attrs={'class':'form-control'}),
        'observacion' : forms.TextInput(attrs={'class':'form-control'}),
        }

#Creacion de Pedidos
class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido

        fields = [
            'titulo',
            'fecha_estimada_entrega',
        ]

        labels = {
            'titulo' : 'titulo',
            'fecha_estimada_entrega' : 'Fecha de Entrega',
            }

        widgets = {
        'titulo' : forms.TextInput(attrs={'class':'form-control'}),
        'fecha_estimada_entrega' : forms.DateField(widget=forms.widgets.DateInput(format="%m/%d/%Y")),
                }
