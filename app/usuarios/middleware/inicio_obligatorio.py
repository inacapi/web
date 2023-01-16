from django.urls import reverse
from django.shortcuts import redirect


class InicioObligatorio(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ruta = request.META.get('PATH_INFO')
        if not 'iniciar_sesion' in ruta and not ruta.startswith('/admin') and not ruta.startswith('/api'):
            if not 'nombre' in request.session or request.session['nombre'] is None:
                return redirect(reverse('usuarios:iniciar_sesion'))

        return self.get_response(request)
