from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from docentes.models import Docente
from docentes.forms import DocenteFormulario
from django.forms import ModelForm
from django.urls import reverse


def crear(request):
    formulario = DocenteFormulario()
    if request.method == 'POST':
        formulario = DocenteFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(reverse('docentes:docentes'))
        else:
            return render(request, 'docentes/crear.html', {
                'formulario': formulario,
                'titulo': 'Crear'
                
            })

    return render(request, 'docentes/crear.html', {
        'formulario': formulario,
        'titulo': 'Crear'

    })


def docentes(request):
    return render(request, 'docentes/docentes.html', {
        'docentes': Docente.objects.all()
    })


def eliminar(request, id):
    docente = Docente.objects.get(id=id)
    docente.delete()
    return redirect(reverse('docentes:docentes'))

def actualizar(request, id):
    docente = Docente.objects.get(id=id)
    formulario = DocenteFormulario(instance=docente)
    if request.method == 'POST':
        formulario = DocenteFormulario(request.POST, instance=docente)
        if formulario.is_valid():
            formulario.save()
            return redirect(reverse('docentes:docentes'))
        else:
            return render(request, 'docentes/docentes.html', {
                'formulario': formulario
            })

    return render(request, 'docentes/crear.html', {
        'formulario': formulario,
        'titulo': 'Actualizar'
    })