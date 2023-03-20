from django import forms

class CursoForm(forms.Form):

    nombre = forms.CharField()
    camada = forms.IntegerField(min_value=1000)


class BusquedaCursoForm(forms.Form):

    nombre = forms.CharField(min_length=3, max_length=40)

class ClientesForm(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()

class ProductoForm(forms.Form):

    producto = forms.CharField()
    categoria = forms.CharField()
    stock = forms.IntegerField()