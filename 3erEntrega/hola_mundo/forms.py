from django import forms

class PersonaForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    fecha_nacimiento = forms.DateField()

class Producto(forms.Form):
    nombre = forms.CharField(max_length=100)
    cantidad = forms.IntegerField()
    id_Producto = forms.IntegerField()

class Venta(forms.Form):
    nombre = forms.CharField(max_length=100)
    cantidad = forms.IntegerField()
    condicion = forms.CharField(max_length=100)
    id_Producto = forms.IntegerField()
    
    
class BuscarPersonasForm(forms.Form):
    criterio_nombre =forms.CharField(max_length=100)

