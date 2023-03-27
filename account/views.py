from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate

from account.forms import UserRegisterForm
from account.models import Avatar


def editar_usuario(request):

    user = request.user

    if request.method == "POST":
        form = UserRegisterForm(request.POST, request.FILES)

        if form.is_valid():
            informacion = form.cleaned_data

            user.username = informacion["username"]
            user.email = informacion["email"]
            user.is_staff = informacion["is_staff"]

            try:
                user.avatar.imagen = informacion["imagen"]
            except:
                avatar = Avatar(user=user, imagen=informacion["imagen"])
                avatar.save()

            user.save()
            return redirect("AccountLogin")

    form = UserRegisterForm(initial={
        "username": user.username,
        "email": user.email,
        "is_staff": user.is_staff
    })

    context = {
        "form": form,
        "titulo": "Editar usuario",
        "Enviar": "Editar"
    }

    return render(request, "form.html", context=context)


def register_account(request):
    if request.method == "POST":
        # form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("AccountLogin")

    # form = UserCreationForm()
    form = UserRegisterForm()
    context = {
        "form": form,
        "titulo": "Registra usuario",
        "Enviar": "Registrar"
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
                return redirect("AppCoderInicio")

    form = AuthenticationForm()
    context = {
        "form": form,
        "titulo": "Login",
        "Enviar": "Iniciar"
    }
    return render(request, "form.html", context=context)