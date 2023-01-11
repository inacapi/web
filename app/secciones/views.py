from django.shortcuts import redirect, render
from django.urls import reverse

from secciones.forms import SeccionFormulario
from secciones.models import Seccion


def crear(request):
    formulario = SeccionFormulario()
    if request.method == 'POST':
        formulario = SeccionFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(reverse('secciones:secciones'))
        else:
            return render(request, 'secciones/crear.html', {
                'formulario': formulario,
                'titulo': 'Crear'
                
            })

    return render(request, 'secciones/crear.html', {
        'formulario': formulario,
        'titulo': 'Crear'

    })

def secciones(request):
    return render(request, 'secciones/secciones.html', {
        'secciones': Seccion.objects.all()
    })

def eliminar(request, id):
    secciones = Seccion.objects.get(id=id)
    secciones.delete()
    return redirect(reverse('secciones:secciones'))

def actualizar(request, id):
    seccion = Seccion.objects.get(id=id)
    formulario = SeccionFormulario(instance=seccion)
    if request.method == 'POST':
        formulario = SeccionFormulario(request.POST, instance=seccion)
        if formulario.is_valid():
            formulario.save()
            return redirect(reverse('secciones:secciones'))
        else:
            return render(request, 'secciones/secciones.html', {
                'formulario': formulario
            })

    return render(request, 'secciones/crear.html', {
        'formulario': formulario,
        'titulo': 'Actualizar'
    })