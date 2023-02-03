from django.urls import reverse
from django.http import HttpRequest
from django.shortcuts import redirect


class InicioObligatorioMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        ruta = request.META.get('PATH_INFO')

        rutas_excluidas = ['/admin/', '/api/', '/usuarios/iniciar_sesion/']

        if not request.user.is_authenticated:
            if not any(ruta.startswith(ruta_excluida) for ruta_excluida in rutas_excluidas):
                return redirect(reverse('usuarios:iniciar_sesion'))

        return self.get_response(request)


class TokenMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        token = request.session.get('token', '')
        request.META['HTTP_AUTHORIZATION'] = f'Token {token}'

        return self.get_response(request)
