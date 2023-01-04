from django.shortcuts import render, redirect
# from estudiantes.models import models
from django.http import HttpResponse
from estudiantes.models import Estudiantes
from estudiantes.forms import EstudiantesFormulario
from django.forms import ModelForm
from django.urls import reverse
# Create your views here.


def crear(request):
    formulario = EstudiantesFormulario()
    if request.method == 'POST':
        formulario = EstudiantesFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(reverse('estudiantes:estudiantes'))
        else:
            return render(request, 'estudiantes/crear.html', {
                'formulario': formulario
            })

    return render(request, 'estudiantes/crear.html', {
        'formulario': formulario

    })


def estudiantes(request):
    return render(request, 'estudiantes/estudiantes.html', {
        'estudiantes': Estudiantes.objects.all()
    })


def eliminar(request, id):
    estudiante = Estudiantes.objects.get(id=id)
    estudiante.delete()
    return redirect(reverse('estudiantes:estudiantes'))

def actualizar(request, id):
    estudiante = Estudiantes.objects.get(id=id)
    formulario = EstudiantesFormulario(instance=estudiante)
    if request.method == 'POST':
        formulario = EstudiantesFormulario(request.POST, instance=estudiante)
        if formulario.is_valid():
            formulario.save()
            return redirect(reverse('estudiantes:estudiantes'))
        else:
            return render(request, 'estudiantes/estudiantes.html', {
                'formulario': formulario
            })

    return render(request, 'estudiantes/actualizar.html', {
        'formulario': formulario
    })