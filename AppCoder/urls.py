from django.http import HttpResponse
from django.urls import path, include
from django.contrib import admin
from AppCoder.views import *



urlpatterns = [

        path('blog', blog, name = "AppCoderBlogs"),
        path('blog/crear', crear_blog, name = "AppCoderCrearBlog"),
        path('busqueda_blog', busqueda_blog, name="AppCoderBuscarBlog"),
        path('blog/eliminar/<titulo>', eliminar_blog, name="AppCoderEliminarBlog"),
        path('blog/editar/<titulo>', editar_blog, name="AppCoderEditarBlog"),
        path('blog/leermas/<int:pk>/', blog_detalles, name='AppCoderLeerMas'),
        path('blog/eliminar_comentario/<int:pk>/', eliminar_comentario, name='AppCoderEliminarComentario'),
        path('about/', about, name="AppCoderAbout")


]