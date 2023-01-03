from django.shortcuts import render
#from estudiantes.models import models
from django.http import HttpResponse
#from estudiantes.models import Estudiantes
from estudiantes.forms import EstudiantesFormulario
from django.forms import ModelForm
# Create your views here.

def crear(request):
    formulario = EstudiantesFormulario()
    if request.method == 'POST':
        formulario = EstudiantesFormulario(request.POST)
        if formulario.is_valid():
            estudiante = formulario.save
        


    return render(request, 'estudiantes/lista.html' , {
        'formulario': formulario
    })




# def eliminar_estudiante(request, id):
#     lista.objects.get(id=id).delete()
#     return HttpResponse('Alumno eliminado')

# def editar_estudiante(request, id):
#     estudiante = lista.objects.get(id=id)
#     if request.method == 'POST':
#         nombre = request.POST.get('nombre')
#         apellido = request.POST.get('apellido')
#         estudiante.nombre = nombre
#         estudiante.apellido = apellido
#         estudiante.save()
#         return HttpResponse('Alumno editado')
#     return render(request, 'estudiantes/editar.html', {
#         'estudiante': estudiante
#     })

def index(request):
    return render(request, 'estudiantes/index.html')