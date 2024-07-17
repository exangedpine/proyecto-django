from django.shortcuts import render
from .forms import ComentarioContactoForm

#Estamos importando la clase Alumno.
from .models import Alumnos 
from .models import ComentarioContacto
from django.shortcuts import get_object_or_404

# Create your views here.

def Principal(request):
    # Esta función recupera todos los modelos de registro
    alumnos = Alumnos.objects.all() 
    return render(request, "registro/principal.html",{'alumnos':alumnos})

def comentarios(request):
    comentarios = ComentarioContacto.objects.all()
    return render(request, "registro/comentarios.html",{'comentarios':comentarios})

def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid(): #Si los datos recibidos son correctos
            form.save() #inserta
            comentarios=ComentarioContacto.objects.all()
            return render(request,"registro/comentarios.html",{'comentarios':comentarios})

    form = ComentarioContactoForm()
    #Si algo sale mal se reenvian al formulario los datos ingresados
    return render(request,'registro/contacto.html',{'form': form})

def contacto(request):
    return render(request,"registro/contacto.html")

def eliminarComentarioContacto(request, id, confirmacion='registro/confirmarEliminacion.html'):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    if request.method=='POST':
        comentario.delete()
        comentarios=ComentarioContacto.objects.all()
        return render(request,"registro/comentarios.html",{'comentarios':comentarios})

    return render(request, confirmacion, {'object':comentario})
    