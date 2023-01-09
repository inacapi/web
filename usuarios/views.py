from django.shortcuts import render, redirect
from django.http import HttpResponse
from inscripciones.models import Inscripcion
from usuarios.models import Usuario
from usuarios.forms import UsuarioFormulario
from django.forms import ModelForm
from django.urls import reverse

from web.helpers import inicio_obligatorio , guardar_sesion, eliminar_sesion

# Create your views here.



def iniciar(request):
    if request.method == 'POST':
        formulario = UsuarioFormulario(request.POST)
        try:
            usuario = Usuario.objects.get(nombre=formulario.data['nombre'], contrasena=formulario.data['contrasena'])
            print(usuario.nombre)
            guardar_sesion(request, usuario)
            return redirect(reverse('inscripciones:inscripciones'))
            
        except Usuario.DoesNotExist:
            return render(request, 'usuarios/iniciar.html', {
                'formulario': formulario,
                'mensaje_error': 'usuario o contraseña incorrecta'
            })

    formulario = UsuarioFormulario()
    return render(request, 'usuarios/iniciar.html', {
        'formulario': formulario

    }
    )

@inicio_obligatorio
def cerrar(request):
    eliminar_sesion(request)
    return redirect(reverse('usuarios:iniciar'))

