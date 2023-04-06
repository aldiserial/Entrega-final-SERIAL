from django.test import TestCase
from django.urls import reverse
from AppCoder.models import Curso


# Create your tests here.
class CursoTestCase(TestCase):
    def setUp(self):
        Curso.objects.create(nombre = "Python1", camada=1)
        Curso.objects.create(nombre="Python2", camada = 2)

    def test_creando_cursos(self):
        p1 = Curso.objects.get(camada=1)
        p2 = Curso.objects.get(camada=2)
        self.assertEqual(p1.nombre, 'Python1')
        self.assertEqual(p2.nombre, 'Python2')

class ViewTests(TestCase):
    def test_no_questions(self):
        response = self.client.get(reverse('AppCoderInicio'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Creación de cursos")

    def test_past_question(self):
        curso = Curso.objects.create(nombre = "Python1", camada=1)
        response = self.client.get(reverse('AppCoderCursos'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,
                            f"curso: Python1 camada: 1")



