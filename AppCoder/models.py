from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from AppCoder.forms import BlogForm
from django.utils import timezone

# Create your models here.
class Blog(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    cuerpo = models.TextField()
    imagen = models.ImageField(upload_to="media", null=True, blank=True)
    fecha = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"El blog {self.titulo} fue escrito por {self.autor}"



class Comentarios(models.Model):
    autor = models.CharField(max_length=200)
    texto = models.TextField()
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE)

