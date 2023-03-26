
from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

    def __str__(self):
        return f'Curso: {self.nombre}, Camada: {self.camada}'

class Clientes(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f'Nombre: {self.nombre} {self.apellido}, Email: {self.email}'
class Producto(models.Model):
    producto = models.CharField(max_length=30, unique=True)
    categoria = models.CharField(max_length=30)
    stock = models.IntegerField()

    def __str__(self):
        return f'Producto: {self.producto}. {self.stock} unidades en stock.'

class Envio(models.Model):
    nombre_apellido = models.CharField(max_length=40)
    calle = models.CharField(max_length=40)
    numero_calle = models.IntegerField()
    localidad = models.CharField(max_length=40)
    provincia = models.CharField(max_length=40)
    codigopostal = models.IntegerField()

    def __str__(self):
        return f'Domicilio: {self.calle} {self.numero_calle}, {self.localidad}, {self.provincia} '