from django.shortcuts import render

from estudiantes.forms import EstudianteFormulario, MatriculaFormulario
from estudiantes.models import Estudiante


def estudiantes(request):
    return render(request, 'estudiantes/estudiantes.html', {
        'estudiantes': Estudiante.objects.all(),
        'formulario': EstudianteFormulario()
    })


def estudiante(request, id):
    estudiante = Estudiante.objects.get(id=id)
    return render(request, 'estudiantes/estudiante.html', {
        'estudiante': estudiante,
        'formulario': MatriculaFormulario(estudiante=estudiante)
    })


def matricula(request, id_estudiante, id_matricula):
    estudiante = Estudiante.objects.get(id=id_estudiante)
    matricula = estudiante.matriculas.get(id=id_matricula)
    return render(request, 'estudiantes/matricula.html', {
        'matricula': matricula
    })
