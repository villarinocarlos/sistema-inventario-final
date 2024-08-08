from django.forms import ModelForm

from .models import Inventario

class InventarioUpdateForm(ModelForm):
    class Meta:
        model = Inventario
        fields = ['nombre', 'descripcion', 'categoria', 'precio', 'stock']


class AddInventarioForm(ModelForm): 
    class Meta:
        model = Inventario
        fields = ["nombre", "descripcion", "categoria", "precio", "stock"]