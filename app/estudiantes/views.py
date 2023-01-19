
from django.shortcuts import redirect, render
from django.urls import reverse
from estudiantes.forms import EstudianteFormulario , MatriculaFormulario
from estudiantes.models import Estudiante



def estudiantes(request):
    return render(request, 'estudiantes/estudiantes.html',{
        'estudiantes': Estudiante.objects.all(),
        'formulario': EstudianteFormulario()
    })




def estudiante(request, id):
    estudiante = Estudiante.objects.get(id=id)
    return render(request, 'estudiantes/estudiante.html', {
        'estudiante': estudiante,
        'formulario': MatriculaFormulario()
    })


def secciones(request, id_estudiante,id_periodo, id_matricula):
    estudiante = Estudiante.objects.get(id=id_estudiante)
    inscripciones = estudiante.matriculas.get(id=id_matricula).inscripciones.all()
    
    return render(request, 'estudiantes/secciones.html', {
        'estudiante': estudiante,
        'inscripciones': inscripciones,
    })

