
from django.urls import path
from AppCoder.views import profesores, cursos, estudiantes

urlpatterns = [
        path('cursos', cursos),
        path('estudiantes', estudiantes),
        path('profesores', profesores),


]