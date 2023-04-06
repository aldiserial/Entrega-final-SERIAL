from django.urls import path, include
from django.contrib import admin
from AppCoder.views import *
from django.conf.urls.static import static
from ProyectoCoder3675 import settings


urlpatterns = [
        path('', inicio, name = "AppCoderInicio"),

        path('admin/', admin.site.urls),
        path('AppCoder/', include('AppCoder.urls')),
        path('account/', include('account.urls')),
        path('about/', about, name="SobreNosotros"),

              ] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)