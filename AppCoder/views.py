from django.http import HttpResponse
from django.shortcuts import render, redirect
from AppCoder.models import *
from AppCoder.forms import BusquedaClienteForm, BusquedaCursoForm, CursoForm, ClientesForm, ProductoForm, EnvioForm


# Create your views here.

def crear_curso(request):
    if request.method == 'POST':
        mi_formulario = CursoForm(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            curso_save = Curso(nombre = informacion ['nombre'],
                               camada = informacion ['camada'])
            curso_save.save()
            return redirect("AppCoderCursos")

    mi_formulario = CursoForm()
    context = {
        "form": mi_formulario
    }
    return render(request, "AppCoder/crear_curso.html", context=context)

def editar_curso(request,camada):
    get_curso = Curso.objects.get(camada=camada)
    if request.method == 'POST':
        mi_formulario = CursoForm(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data

            get_curso.nombre = informacion ['nombre']
            get_curso.camada= informacion ['camada']

            get_curso.save()
            return redirect("AppCoderCursos")


    context = {
        "camada": camada,
        "form": CursoForm (initial = {
            'nombre': get_curso.nombre,
            'camada': get_curso.camada
        })
    }
    return render(request, "AppCoder/editar_curso.html", context=context)
def cursos(request):

    all_cursos = Curso.objects.all()
    context = {
        "cursos": all_cursos,
        "form_busqueda": BusquedaCursoForm()
    }
    return render(request, 'AppCoder/Cursos.html', context=context)


def busqueda_curso(request):
    mi_formulario = BusquedaCursoForm(request.GET)
    if mi_formulario.is_valid():
        informacion = mi_formulario.cleaned_data
        cursos_filtrados = Curso.objects.filter(nombre__icontains=informacion['nombre'])
        context = {
            "cursos": cursos_filtrados
        }
        return render(request, "AppCoder/busqueda_curso.html", context=context)

def busqueda_cliente(request):
    mi_formulario = BusquedaClienteForm(request.GET)
    if mi_formulario.is_valid():
        informacion = mi_formulario.cleaned_data
        emails_filtrados = Clientes.objects.filter(email__icontains=informacion['email'])

        context = {
            "clientes": emails_filtrados
        }
        return render(request, "AppCoder/busqueda_cliente.html", context=context)
def eliminar_curso(request, camada):
    get_curso = Curso.objects.get(camada=camada)
    get_curso.delete()
    return redirect("AppCoderCursos")


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
        "form": ClientesForm(),
        "form_busqueda": BusquedaClienteForm()

    }
    return render(request, 'AppCoder/Clientes.html', context=context)

def crear_cliente (request, nombre, apellido, email):
    save_cliente = Clientes(nombre = nombre, apellido = apellido, email = email)
    save_cliente.save()
    context = {
        "nombre": nombre,
        "apellido": apellido,
        "email": email
            }
    return render(request, "AppCoder/save_cliente.html", context)




def inicio(request):
   return render(request, "AppCoder/Inicio.html")




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

def crear_producto (request, nombre, categoria, stock):
    save_producto = Producto(producto = producto, categoria = categoria, stock = int(stock))
    save_producto.save()
    context = {
        "Producto ": producto,
        "Categoría ": categoria,
        "Stock ": stock
    }
    return render(request, "AppCoder/save_producto.html", context)
def envio(request):
    if request.method == 'POST':
        mi_formulario = EnvioForm(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            envio_save = Envio(nombre_apellido= informacion ['nombre_apellido'],
                               calle = informacion ["calle"],
                                numero_calle = informacion ["numero_calle"],
                               localidad = informacion ["localidad"],
                               provincia = informacion ["provincia"],
                               codigopostal = informacion ["codigopostal"],)
            envio_save.save()


    all_envios = Envio.objects.all()
    context = {
        "envio": all_envios,
        "form": EnvioForm()

    }
    return render(request, 'AppCoder/Envio.html', context=context)

def crear_envio (request, nombre_apellido, calle, numero_calle, localidad, provincia, codigopostal):
    save_envio = Envio(nombre_apellido = nombre_apellido, calle = calle, numero_calle = int(numero_calle),
                       localidad = localidad, provincia = provincia, codigopostal = int(codigopostal))
    save_envio.save()
    context = {
        "Nombre y apellido ": nombre_apellido,
        "Calle ": calle,
        "Número ": numero_calle,
        "Localidad ": localidad,
        "Provincia ": provincia,
        "Código Postal ": codigopostal

    }
    return render(request, "AppCoder/save_envio.html", context)