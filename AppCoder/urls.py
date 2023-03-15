
from django.urls import path
from django.contrib import admin
from AppCoder.views import cursos, crear_curso, estudiantes, profesores

urlpatterns = [
        path('admin/', admin.site.urls),
        path('cursos', cursos, name = "AppCoderCursos"),
        path('curso/<nombre>/<camada>', crear_curso, name = "AppCoderCurso"),
        path('estudiantes', estudiantes, name = "AppCoderEstudiantes"),
        path('profesores', profesores, name = "AppCoderProfesores"),
]