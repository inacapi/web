from django.shortcuts import render

from clases.models import Clase


def clases(request):
    return render(request, 'clases/clases.html', {
        'clases': Clase.objects.all()
    })


def clase(request, id_clase):
    clase = Clase.objects.get(id=id_clase)
    return render(request, 'clases/clase.html', {
        'clase': clase
    })
