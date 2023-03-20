from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField(unique=True)

    def __str__(self):
        return f'Curso: {self.nombre}, Camada: {self.camada}'

class Clientes(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f'Nombre: {self.nombre}, Apellido: {self.apellido}, Email: {self.email}'
class Producto(models.Model):
    producto = models.CharField(max_length=30)
    categoria = models.CharField(max_length=30)
    stock = models.IntegerField()

    def __str__(self):
        return f'Producto: {self.producto}. {self.stock} unidades en stock.'