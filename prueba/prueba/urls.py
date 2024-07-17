"""
URL configuration for prueba project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inicio import views
from django.conf import settings
from registro import views as views_registro

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views_registro.Principal, name="Principal"),
    path('contacto/',views_registro.contacto,name="Contacto"),
    path('comentarios/',views_registro.comentarios,name="Comentarios"),
    path('formulario/', views.formulario, name="Formulario"),
    path('registrar/',views_registro.registrar,name="Registrar"),
    path('eliminarComentario/<int:id>/',views_registro.eliminarComentarioContacto, name='Eliminar'),
]

if settings.DEBUG:
    from django.conf.urls.static import static 
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
