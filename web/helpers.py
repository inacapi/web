from django.shortcuts import redirect
from functools import wraps


def inicio_obligatorio(funcion, ruta_redireccion='usuarios:iniciar'):
    @wraps(funcion)
    def funcion_decorada(request, *args, **kwargs):
        if 'nombre' in request.session and not request.session['nombre'] is None:
            return funcion(request, *args, **kwargs)
        else:
            return redirect(ruta_redireccion)
    return funcion_decorada


def guardar_sesion(request, usuario):
    request.session['nombre'] = usuario.nombre


def eliminar_sesion(request):
    request.session['nombre'] = None
