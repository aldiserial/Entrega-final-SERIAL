from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from account.views import *
from django.contrib.auth.views import LogoutView
from django.conf import settings

urlpatterns = [
    path('editar/usuario/', editar_usuario, name="AccountEditarUsuario"),
    path('login/', login_account, name="AccountLogin"),
    path('register/', register_account, name="AccountRegister"),

    path('logout/', LogoutView.as_view(template_name="account/logout.html"), name="AccountLogout")
] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)