from django.shortcuts import render , redirect
from django.http import HttpResponse
from inscripciones.models import Inscripcion
from inscripciones.forms import IncripcionFormulario
from django.forms import ModelForm
from django.urls import reverse



def crear(request):
    formulario = IncripcionFormulario()
    if request.method == 'POST':
        formulario = IncripcionFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(reverse('inscripciones:inscripciones'))
        else:
            return render(request, 'inscripciones/crear.html', {
                'formulario': formulario,
                'titulo': 'Crear'
                
            })

    return render(request, 'inscripciones/crear.html', {
        'formulario': formulario,
        'titulo': 'Crear'

    })


def inscripciones(request):
    return render(request, 'inscripciones/inscripciones.html', {
        'inscripciones': Inscripcion.objects.all()
    })


def eliminar(request, id):
    inscripciones = Inscripcion.objects.get(id=id)
    inscripciones.delete()
    return redirect(reverse('inscripciones:inscripciones'))

def actualizar(request, id):
    inscripcion = Inscripcion.objects.get(id=id)
    formulario = IncripcionFormulario(instance=inscripcion)
    if request.method == 'POST':
        formulario = IncripcionFormulario(request.POST, instance=inscripcion)
        if formulario.is_valid():
            formulario.save()
            return redirect(reverse('inscripciones:inscripciones'))
        else:
            return render(request, 'inscripciones/inscripciones.html', {
                'formulario': formulario
            })

    return render(request, 'inscripciones/crear.html', {
        'formulario': formulario,
        'titulo': 'Actualizar'
    })