from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from clases.models import Clase
from clases.forms import ClaseFormulario
from django.forms import ModelForm
from django.urls import reverse


def crear(request):
    formulario = ClaseFormulario()
    if request.method == 'POST':
        formulario = ClaseFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(reverse('clases:clases'))
        else:
            return render(request, 'clases/crear.html', {
                'formulario': formulario,
                'titulo': 'Crear'
                
            })

    return render(request, 'clases/crear.html', {
        'formulario': formulario,
        'titulo': 'Crear'

    })


def clases(request):
    return render(request, 'clases/clases.html', {
        'clases': Clase.objects.all()
    })


def eliminar(request, id):
    clase = Clase.objects.get(id=id)
    clase.delete()
    return redirect(reverse('clases:clases'))

def actualizar(request, id):
    clase = Clase.objects.get(id=id)
    formulario = ClaseFormulario(instance=clase)
    if request.method == 'POST':
        formulario = ClaseFormulario(request.POST, instance=clase)
        if formulario.is_valid():
            formulario.save()
            return redirect(reverse('clases:clases'))
        else:
            return render(request, 'clases/clases.html', {
                'formulario': formulario
            })

    return render(request, 'clases/crear.html', {
        'formulario': formulario,
        'titulo': 'Actualizar'
    })