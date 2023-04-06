from django.http import HttpResponse
from django.urls import path, include
from django.contrib import admin
from AppCoder.views import *

urlpatterns = [

        path('cursos', cursos, name = "AppCoderCursos"),
        path('cursos/crear', crear_curso, name = "AppCoderCrearCursos"),
        path('busqueda_curso', busqueda_curso, name="AppCoderBuscarCurso"),
        path('cursos/eliminar/<camada>', eliminar_curso, name="AppCoderEliminarCurso"),
        path('cursos/editar/<camada>', editar_curso, name="AppCoderEditarCurso"),
        path('busqueda_cliente', busqueda_cliente, name="AppCoderBuscarCliente"),
        path('clientes', clientes, name = "AppCoderClientes"),
        path('producto', producto, name = "AppCoderProductos"),
        path('envio', envio, name="AppCoderEnvio")


]