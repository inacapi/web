from django.shortcuts import render , redirect
from django.http import HttpResponse
from evaluaciones.models import Evaluacion
from evaluaciones.forms import EvaluacionFormulario
from django.forms import ModelForm
from django.urls import reverse



def crear(request):
    formulario = EvaluacionFormulario()
    if request.method == 'POST':
        formulario = EvaluacionFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(reverse('evaluaciones:evaluaciones'))
        else:
            return render(request, 'evaluaciones/crear.html', {
                'formulario': formulario,
                'titulo': 'Crear'
                
            })

    return render(request, 'evaluaciones/crear.html', {
        'formulario': formulario,
        'titulo': 'Crear'

    })


def evaluaciones(request):
    return render(request, 'evaluaciones/evaluaciones.html', {
        'evaluaciones': Evaluacion.objects.all()
    })


def eliminar(request, id):
    evaluaciones = Evaluacion.objects.get(id=id)
    evaluaciones.delete()
    return redirect(reverse('evaluaciones:evaluaciones'))

def actualizar(request, id):
    evaluaciones = Evaluacion.objects.get(id=id)
    formulario = EvaluacionFormulario(instance=evaluaciones)
    if request.method == 'POST':
        formulario = EvaluacionFormulario(request.POST, instance=evaluaciones)
        if formulario.is_valid():
            formulario.save()
            return redirect(reverse('evaluaciones:evaluaciones'))
        else:
            return render(request, 'evaluaciones/evaluaciones.html', {
                'formulario': formulario
            })

    return render(request, 'evaluaciones/crear.html', {
        'formulario': formulario,
        'titulo': 'Actualizar'
    })