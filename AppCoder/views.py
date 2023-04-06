from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from AppCoder.models import Blog, Comentarios
from AppCoder.forms import BusquedaBlogForm, BlogForm, ComentarioForm


# Create your views here.
def blog(request):

    all_blogs = Blog.objects.all()
    context = {
        "blogs": all_blogs,
        "form_busqueda": BusquedaBlogForm()
    }
    return render(request, 'AppCoder/Blogs.html', context=context)

@login_required
def crear_blog(request):
    if request.method == 'POST':
        mi_formulario = BlogForm(request.POST, request.FILES)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            blog_save = Blog(titulo = informacion ['titulo'],
                                subtitulo = informacion ['subtitulo'],
                             cuerpo = informacion['cuerpo'],
                             autor = informacion['autor'],
                             imagen=informacion['imagen']
                             )
            blog_save.save()
            return redirect("AppCoderBlogs")

    mi_formulario = BlogForm()
    context = {
        "form": mi_formulario
    }
    return render(request, "AppCoder/crear_blog.html", context=context)

@user_passes_test(lambda user: user.is_superuser)
def editar_blog(request, titulo):
    blog = Blog.objects.get(titulo=titulo)
    if request.method == 'POST':
        formulario = BlogForm(request.POST, request.FILES)
        if formulario.is_valid():
            blog.titulo = formulario.cleaned_data['titulo']
            blog.subtitulo = formulario.cleaned_data['subtitulo']
            blog.cuerpo = formulario.cleaned_data['cuerpo']
            blog.autor = formulario.cleaned_data['autor']

            if formulario.cleaned_data['imagen']:
                blog.imagen = formulario.cleaned_data['imagen']

            blog.save()
            return redirect('AppCoderBlogs')
    else:
        formulario = BlogForm(initial={
            'titulo': blog.titulo,
            'subtitulo': blog.subtitulo,
            'cuerpo': blog.cuerpo,
            'autor': blog.autor,
            'imagen': blog.imagen,
        })
    return render(request, 'AppCoder/editar_blog.html', {'formulario': formulario, 'blog': blog })




def busqueda_blog(request):
    mi_formulario = BusquedaBlogForm(request.GET)
    if mi_formulario.is_valid():
        informacion = mi_formulario.cleaned_data
        blogs_filtrados = Blog.objects.filter(titulo__icontains=informacion['titulo'])
        context = {
            "blogs": blogs_filtrados
        }
        return render(request, "AppCoder/busqueda_blog.html", context=context)
@user_passes_test(lambda user: user.is_superuser)
def eliminar_blog(request, titulo):
    get_blog = Blog.objects.get(titulo=titulo)
    get_blog.delete()
    return redirect("AppCoderBlogs")

def blog_detalles(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    comentario = Comentarios.objects.filter(blog=blog)

    if request.method == 'POST':
        mi_formulario = ComentarioForm(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            comentario_save = Comentarios(autor=informacion['autor'],
                             texto=informacion['texto'],
                             blog=blog
                             )

            comentario_save.save()
            return redirect("AppCoderLeerMas", pk=blog.id)
        else:
            print(mi_formulario.errors)
    else:
        mi_formulario = ComentarioForm()

    context = {
        "form": mi_formulario,
        "blog": blog,
        "comentario": comentario
    }

    return render(request, 'AppCoder/leermas_blog.html', context=context)
@login_required
def eliminar_comentario(request, pk):
    comentario = get_object_or_404(Comentarios, pk=pk)
    blog_id = comentario.blog.id
    comentario.delete()
    return redirect("AppCoderLeerMas", pk=blog_id)


def inicio(request):
   return render(request, "AppCoder/Inicio.html")

def about(request):
    return render(request, "AppCoder/about.html")

def noregistrado(request):
    return render(request, "AppCoder/noregistrado.html")