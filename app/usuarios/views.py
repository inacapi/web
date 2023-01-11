from django.shortcuts import redirect, render
from django.urls import reverse

from usuarios.forms import UsuarioFormulario
from usuarios.functions import guardar_sesion, limpiar_sesion
from usuarios.models import Usuario


def iniciar_sesion(request):
    if request.method == 'POST':
        formulario = UsuarioFormulario(request.POST)
        try:
            usuario = Usuario.objects.get(
                nombre=formulario.data['nombre'], contrasena=formulario.data['contrasena'])
            guardar_sesion(request, usuario)
            return redirect(reverse('estudiantes:estudiantes'))
        except Usuario.DoesNotExist:
            return render(request, 'usuarios/iniciar_sesion.html', {
                'formulario': formulario,
                'mensaje_error': 'usuario o contraseña incorrecta'
            })

    formulario = UsuarioFormulario()
    return render(request, 'usuarios/iniciar_sesion.html', {
        'formulario': formulario
    })


def cerrar_sesion(request):
    limpiar_sesion(request)
    return redirect(reverse('usuarios:iniciar_sesion'))
