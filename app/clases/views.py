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


def seccion(request, id_clase, id_periodo, id_seccion):
    clase = Clase.objects.get(id=id_clase)
    seccion = clase.secciones.get(id=id_seccion)
    return render(request, 'clases/seccion.html', {
        'seccion': seccion
    })
