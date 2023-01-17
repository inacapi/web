
from django.shortcuts import redirect, render
from django.urls import reverse
from estudiantes.forms import EstudianteFormulario
from estudiantes.models import Estudiante



def estudiantes(request):
    return render(request, 'estudiantes/estudiantes.html',{
        'estudiantes': Estudiante.objects.all(),
        'formulario': EstudianteFormulario()
    })




def estudiante(request, id):
    estudiante = Estudiante.objects.get(id=id)
    return render(request, 'estudiantes/estudiante.html', {
        'estudiante': estudiante
    })


def seccion_estudiante(request, id, matricula):
    estudiante = Estudiante.objects.get(id=id)
    inscripciones = estudiante.matriculas.get(id=matricula).inscripciones.all()
    
    return render(request, 'estudiantes/seccion_estudiante.html', {
        'estudiante': estudiante,
        'inscripciones': inscripciones,
    })

