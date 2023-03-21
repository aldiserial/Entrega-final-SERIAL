from django import forms

class CursoForm(forms.Form):

    nombre = forms.CharField(min_length=3, max_length=40)
    camada = forms.IntegerField(min_value=1000)


class BusquedaCursoForm(forms.Form):

    nombre = forms.CharField(min_length=3, max_length=40)

class ClientesForm(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()

class BusquedaClienteForm(forms.Form):

    nombrecliente = forms.CharField(min_length=3, max_length=40)
class ProductoForm(forms.Form):

    producto = forms.CharField()
    categoria = forms.CharField()
    stock = forms.IntegerField()

class EnvioForm(forms.Form):
    nombre_apellido = forms.CharField(max_length=40)
    calle = forms.CharField(max_length=40)
    numero_calle = forms.IntegerField()
    localidad = forms.CharField(max_length=40)
    provincia = forms.CharField(max_length=40)
    codigopostal = forms.IntegerField()