from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.conf import settings
from account.forms import UserRegisterForm
from account.models import Avatar
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from django.core.files.storage import default_storage

def editar_usuario(request):
    user = request.user

    if request.method == "POST":
        form = UserRegisterForm(request.POST, request.FILES, instance=user)

        if form.is_valid():
            informacion = form.cleaned_data

            user.username = informacion["username"]
            user.email = informacion["email"]
            user.save()

            if not hasattr(user, 'avatar'):
                avatar = Avatar(user=user)
                avatar.save()

            if informacion.get("imagen"):
                user.avatar.imagen = informacion["imagen"]
                user.avatar.save()

            return redirect("AccountLogin")
    else:
        form = UserRegisterForm(instance=user)

    context = {
        "form": form,
        "titulo": "Editar usuario",
        "enviar": "Editar"
    }

    return render(request, "form.html", context=context)


def register_account(request):
    if request.method == "POST":
        # form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("AppCoderInicio")

    # form = UserCreationForm()
    form = UserRegisterForm()
    context = {
        "form": form,
        "titulo": "Registra usuario",
        "enviar": "Registrar"
    }
    return render(request, "form.html", context=context)


def login_account(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            informacion = form.cleaned_data

            user = authenticate(username=informacion['username'], password=informacion['password'])
            if user:
                login(request, user)

                return redirect("AppCoderInicio")
            else:
                return redirect("AccountBlog")

    form = AuthenticationForm()
    context = {
        "form": form,
        "titulo": "Login",
        "enviar": "Iniciar"
    }
    return render(request, "form.html", context=context)