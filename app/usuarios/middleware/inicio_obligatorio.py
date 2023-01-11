from django.urls import reverse
from django.shortcuts import redirect


class InicioObligatorio(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        if not 'iniciar_sesion' in request.META.get('PATH_INFO'):
            if not 'nombre' in request.session or request.session['nombre'] is None:
                return redirect(reverse('usuarios:iniciar_sesion'))
        return None
