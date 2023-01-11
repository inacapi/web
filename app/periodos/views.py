from django.shortcuts import redirect, render
from django.urls import reverse

from periodos.forms import PeriodoFormulario
from periodos.models import Periodo


def crear(request):
    formulario = PeriodoFormulario()
    if request.method == 'POST':
        formulario = PeriodoFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(reverse('periodos:periodos'))
        else:
            return render(request, 'periodos/crear.html', {
                'formulario': formulario,
                'titulo': 'Crear'
                
            })

    return render(request, 'periodos/crear.html', {
        'formulario': formulario,
        'titulo': 'Crear'

    })

def periodos(request):
    return render(request, 'periodos/periodos.html', {
        'periodos': Periodo.objects.all()
    })

def eliminar(request, id):
    periodos = Periodo.objects.get(id=id)
    periodos.delete()
    return redirect(reverse('periodos:periodos'))

def actualizar(request, id):
    periodos = Periodo.objects.get(id=id)
    formulario = PeriodoFormulario(instance=periodos)
    if request.method == 'POST':
        formulario = PeriodoFormulario(request.POST, instance=periodos)
        if formulario.is_valid():
            formulario.save()
            return redirect(reverse('periodos:periodos'))
        else:
            return render(request, 'periodos/periodos.html', {
                'formulario': formulario
            })

    return render(request, 'periodos/crear.html', {
        'formulario': formulario,
        'titulo': 'Actualizar'
    })