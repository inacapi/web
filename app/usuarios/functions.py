def guardar_sesion(request, usuario):
    request.session['nombre'] = usuario.nombre


def limpiar_sesion(request):
    request.session['nombre'] = None
