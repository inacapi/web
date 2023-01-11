from django.shortcuts import redirect, render
from django.urls import reverse

from estudiantes.forms import DocenteFormulario
from estudiantes.models import Estudiante


def crear(request):
    formulario = DocenteFormulario()
    if request.method == 'POST':
        formulario = DocenteFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(reverse('estudiantes:estudiantes'))
        else:
            return render(request, 'estudiantes/crear.html', {
                'formulario': formulario,
                'titulo': 'Crear'
                
            })

    return render(request, 'estudiantes/crear.html', {
        'formulario': formulario,
        'titulo': 'Crear'

    })


def estudiantes(request):
    return render(request, 'estudiantes/estudiantes.html', {
        'estudiantes': Estudiante.objects.all()
    })

def eliminar(request, id):
    estudiante = Estudiante.objects.get(id=id)
    estudiante.delete()
    return redirect(reverse('estudiantes:estudiantes'))

def actualizar(request, id):
    estudiante = Estudiante.objects.get(id=id)
    formulario = DocenteFormulario(instance=estudiante)
    if request.method == 'POST':
        formulario = DocenteFormulario(request.POST, instance=estudiante)
        if formulario.is_valid():
            formulario.save()
            return redirect(reverse('estudiantes:estudiantes'))
        else:
            return render(request, 'estudiantes/estudiantes.html', {
                'formulario': formulario
            })

    return render(request, 'estudiantes/crear.html', {
        'formulario': formulario,
        'titulo': 'Actualizar'
    })