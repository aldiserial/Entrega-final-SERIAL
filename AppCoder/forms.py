from django import forms

from AppCoder.models import *


class BlogForm(forms.Form):
    titulo = forms.CharField(max_length=200)
    subtitulo = forms.CharField(max_length=200)
    autor = forms.CharField(max_length=200)
    cuerpo = forms.CharField(widget=forms.Textarea)
    imagen = forms.ImageField(required=False)



class BusquedaBlogForm(forms.Form):

    titulo = forms.CharField(min_length=3, max_length=40)

class ComentarioForm(forms.Form):
    autor = forms.CharField(max_length=100)
    texto = forms.CharField(widget=forms.Textarea)

    def save(self, blog, commit=True):
        comentario = Comentarios(
            autor=self.cleaned_data['autor'],
            texto=self.cleaned_data['texto'],
            blog=blog
        )
        if commit:
            comentario.save()
        return comentario

    def __init__(self, *args, **kwargs):
        super(ComentarioForm, self).__init__(*args, **kwargs)
        self.fields['blog_id'].widget = forms.HiddenInput()

    blog_id = forms.IntegerField()
class ClientesForm(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()

class BusquedaClienteForm(forms.Form):

    email = forms.EmailField()
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