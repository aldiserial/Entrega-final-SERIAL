from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate

from account.forms import UserRegisterForm


# Create your views here.
def register_account(request):
    if request.method=="POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("AccountLogin")

    form = UserRegisterForm()
    context = {
            "form": form
        }
    return render(request, "account/login.html", context=context)

def login_account(request):

    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)

        if form.is_valid():
            informacion = form.cleaned_data

            user = authenticate(username=informacion['username'],
                                password=informacion['password'])
            if user is not None:
                login(request, user)

                return redirect("AppCoderInicio")

            else:
                return redirect("AppCoderInicio")

    form = AuthenticationForm()
    context= {
        "form": form
    }
    return render(request, "account/login.html", context=context)

