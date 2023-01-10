from django.shortcuts import render , redirect
from django.http import HttpResponse
from matriculas.models import Matricula
from matriculas.forms import MatriculaFormulario
from django.forms import ModelForm
from django.urls import reverse
from web.helpers import inicio_obligatorio

@inicio_obligatorio
def crear(request):
    formulario = MatriculaFormulario()
    if request.method == 'POST':
        formulario = MatriculaFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(reverse('matriculas:matriculas'))
        else:
            return render(request, 'matriculas/crear.html', {
                'formulario': formulario,
                'titulo': 'Crear'
                
            })

    return render(request, 'matriculas/crear.html', {
        'formulario': formulario,
        'titulo': 'Crear'

    })


@inicio_obligatorio
def matriculas(request):
    return render(request, 'matriculas/matriculas.html', {
        'matriculas': Matricula.objects.all()
    })

@inicio_obligatorio
def eliminar(request, id):
    matriculas = Matricula.objects.get(id=id)
    matriculas.delete()
    return redirect(reverse('matriculas:matriculas'))

@inicio_obligatorio
def actualizar(request, id):
    matricula = Matricula.objects.get(id=id)
    formulario = MatriculaFormulario(instance=matricula)
    if request.method == 'POST':
        formulario = MatriculaFormulario(request.POST, instance=matricula)
        if formulario.is_valid():
            formulario.save()
            return redirect(reverse('matriculas:matriculas'))
        else:
            return render(request, 'matriculas/matricula.html', {
                'formulario': formulario
            })

    return render(request, 'matriculas/crear.html', {
        'formulario': formulario,
        'titulo': 'Actualizar'
    })