from django import forms
from apps.order.models import  Item, Pedido

#class CustomClearableFileInput(ClearableFileInput):
#    template_with_clear = "<br>  <label for='%(clear_checkbox_id)s'>%(clear_checkbox_label)s</label> %(clear)s"

# Creacion de Items
class ItemForm(forms.ModelForm):
    class Meta:
        model = Item

        fields = [
            'pedido',
            'sys_impr',
            'tipo_material',
            'impresion',
            'archivo',
            'cantidad',
            'observacion',
        ]

        labels = {
            'pedido' : 'pedido',
            'sys_impr' : 'Sistema de Impresion',
            'tipo_material' : 'Tipo de Material',
            'impresion' : 'Impresion',
            'archivo' : 'Imagen o Zip con imagenes',
            'cantidad' : 'Cantidad',
            'observacion' : 'Detalles',
        }

        widgets = {
        'pedido' : forms.TextInput(attrs={'class':'form-control'}),
        'sys_impr' : forms.Select(attrs={'class':'form-control'}),
        'tipo_material' : forms.Select(attrs={'class':'form-control'}),
        'impresion' : forms.Select(attrs={'class':'form-control'}),
        'archivo': forms.ClearableFileInput(attrs={'multiple': True}),
        'cantidad': forms.TextInput(attrs={'class':'form-control'}),
        'observacion' : forms.Textarea(attrs={'class':'form-control'}),
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
