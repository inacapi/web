from django.shortcuts import redirect, render
from django.urls import reverse

from estudiantes.forms import DocenteFormulario
from estudiantes.models import Estudiante



def estudiantes(request):
    return render(request, 'estudiantes/estudiantes.html', {
        'estudiantes': Estudiante.objects.all()
    })




def detalle_estudiante(request, id):
    estudiante = Estudiante.objects.get(id=id)
    return render(request, 'estudiantes/detalle_estudiante.html', {
        'estudiante': estudiante
    })
