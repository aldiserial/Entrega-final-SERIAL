
from django.urls import path
from AppCoder.views import cursos, crear_curso, estudiantes, profesores

urlpatterns = [
        path('cursos', cursos, name = "AppCoderCursos"),
        path('curso/<nombre>/<camada>', crear_curso, name = "AppCoderCurso"),
        path('estudiantes', estudiantes, name = "AppCoderEstudiantes"),
        path('profesores', profesores, name = "AppCoderProfesores"),
]