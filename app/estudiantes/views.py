from django.shortcuts import render, redirect
# from estudiantes.models import models
from django.http import HttpResponse
from estudiantes.models import Estudiante
from estudiantes.forms import DocenteFormulario
from django.forms import ModelForm
from django.urls import reverse
from web.helpers import inicio_obligatorio

@inicio_obligatorio
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


@inicio_obligatorio
def estudiantes(request):
    return render(request, 'estudiantes/estudiantes.html', {
        'estudiantes': Estudiante.objects.all()
    })

@inicio_obligatorio
def eliminar(request, id):
    estudiante = Estudiante.objects.get(id=id)
    estudiante.delete()
    return redirect(reverse('estudiantes:estudiantes'))

@inicio_obligatorio
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