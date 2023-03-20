"""ProyectoCoder3675 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin
from AppCoder.views import *

urlpatterns = [
        path('', include('admin_soft.urls')),
        path('admin/', admin.site.urls),
        path('cursos', cursos, name = "AppCoderCursos"),
        path('buscar_curso', busqueda_curso, name="AppCoderBuscarCurso"),
        path('curso/<nombre>/<camada>', crear_curso, name = "AppCoderCurso"),
        path('estudiantes', estudiantes, name = "AppCoderEstudiantes"),
        path('profesores', profesores, name = "AppCoderProfesores"),
]