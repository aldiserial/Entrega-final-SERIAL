
from django.urls import path, include
from django.contrib import admin
from AppCoder.views import *

urlpatterns = [
        path('', include('admin_soft.urls')),
        path('admin/', admin.site.urls),
        path('buscar_curso', busqueda_curso, name="AppCoderBuscarCurso"),
        path('cursos', cursos, name = "AppCoderCursos"),
        path('curso/<nombre>/<camada>', crear_curso, name = "AppCoderCurso"),
        path('estudiantes', estudiantes, name = "AppCoderEstudiantes"),
        path('profesores', profesores, name = "AppCoderProfesores"),
]