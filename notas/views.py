from django.shortcuts import render , redirect
from django.http import HttpResponse
from notas.models import Nota
from notas.forms import NotaFormulario
from django.forms import ModelForm
from django.urls import reverse
from web.helpers import inicio_obligatorio

@inicio_obligatorio
def crear(request):
    formulario = NotaFormulario()
    if request.method == 'POST':
        formulario = NotaFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(reverse('notas:notas'))
        else:
            return render(request, 'notas/crear.html', {
                'formulario': formulario,
                'titulo': 'Crear'
                
            })

    return render(request, 'notas/crear.html', {
        'formulario': formulario,
        'titulo': 'Crear'

    })

@inicio_obligatorio
def notas(request):
    return render(request, 'notas/notas.html', {
        'notas': Nota.objects.all()
    })

@inicio_obligatorio
def eliminar(request, id):
    notas = Nota.objects.get(id=id)
    notas.delete()
    return redirect(reverse('notas:notas'))

@inicio_obligatorio
def actualizar(request, id):
    nota = Nota.objects.get(id=id)
    formulario = NotaFormulario(instance=nota)
    if request.method == 'POST':
        formulario = NotaFormulario(request.POST, instance=nota)
        if formulario.is_valid():
            formulario.save()
            return redirect(reverse('notas:notas'))
        else:
            return render(request, 'notas/notas.html', {
                'formulario': formulario
            })

    return render(request, 'notas/crear.html', {
        'formulario': formulario,
        'titulo': 'Actualizar'
    })