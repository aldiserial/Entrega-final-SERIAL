from django.http import HttpResponse
from django.shortcuts import render, redirect
from AppCoder.models import Curso, Clientes, Producto
from AppCoder.forms import CursoForm, BusquedaCursoForm, ClientesForm, ProductoForm


# Create your views here.
def busqueda_curso(request):
    mi_formulario = BusquedaCursoForm(request.GET)
    if mi_formulario.is_valid():
        informacion = mi_formulario.cleaned_data
        cursos_filtrados = Curso.objects.filter(nombre__icontains=informacion['nombre'])
        context = {
            "cursos": cursos_filtrados
        }
        return render(request, "AppCoder/busqueda_curso.html", context=context)

def cursos(request):
    if request.method == 'POST':
        mi_formulario = CursoForm(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            curso_save = Curso(nombre = informacion ['nombre'],
                               camada = informacion ["camada"])
            curso_save.save()


    all_cursos = Curso.objects.all()
    context = {
        "cursos": all_cursos,
        "form": CursoForm(),
        "form_busqueda": BusquedaCursoForm()
    }
    return render(request, 'AppCoder/cursos.html', context=context)

def clientes(request):
    if request.method == 'POST':
        mi_formulario = ClientesForm(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            cliente_save = Clientes(nombre = informacion ['nombre'],
                               apellido = informacion ["apellido"],
                                email = informacion ["email"])
            cliente_save.save()


    all_clientes = Clientes.objects.all()
    context = {
        "clientes": all_clientes,
        "form": ClientesForm()

    }
    return render(request, 'AppCoder/Clientes.html', context=context)

def inicio(request):
   return render(request, "base.html")



def crear_curso (request, nombre, camada):
    save_curso = Curso(nombre = nombre, camada = int(camada))
    save_curso.save()
    context = {
        "nombre": nombre
    }
    return render(request, "AppCoder/save_curso.html", context)

def crear_cliente (request, nombre, apellido, email):
    save_cliente = Clientes(nombre = nombre, apellido = apellido, email = email)
    save_cliente.save()
    context = {
        "nombre": nombre,
        "apellido": apellido,
        "email": email
            }
    return render(request, "AppCoder/save_cliente.html", context)
def producto(request):
    if request.method == 'POST':
        mi_formulario = ProductoForm(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            producto_save = Producto(producto = informacion ['producto'],
                               categoria = informacion ["categoria"],
                                stock = informacion ["stock"])
            producto_save.save()


    all_productos = Producto.objects.all()
    context = {
        "productos": all_productos,
        "form": ProductoForm()

    }
    return render(request, 'AppCoder/Productos.html', context=context)