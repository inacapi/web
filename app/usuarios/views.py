from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.urls import reverse
from usuarios.forms import UsuarioFormulario
from rest_framework.authtoken.models import Token


def iniciar_sesion(request):
    formulario = UsuarioFormulario()

    if request.method == 'POST':
        formulario = UsuarioFormulario(request.POST)

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            token, _ = Token.objects.get_or_create(user=user)
            request.session['token'] = token.key

            return redirect(reverse('estudiantes:estudiantes'))

        else:
            return render(request, 'usuarios/iniciar_sesion.html', {
                'formulario': formulario,
                'mensaje_error': 'Nombre de usuario o contraseña incorrecta'
            })

    return render(request, 'usuarios/iniciar_sesion.html', {
        'formulario': formulario
    })


def cerrar_sesion(request):
    logout(request)
    return redirect(reverse('usuarios:iniciar_sesion'))
