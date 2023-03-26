from django.http import HttpResponse
from django.urls import path, include
from django.contrib import admin
from account.views import login_account, register_account
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_account, name="AccountLogin"),
    path('register/', register_account, name="AccountRegister"),
    path('logout/', LogoutView.as_view(template_name="account/logout.html"), name="AccountLogout")
]