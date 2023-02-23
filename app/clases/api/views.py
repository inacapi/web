import json

from rest_framework.decorators import api_view
from rest_framework.response import Response

from clases.models import Clase
from estudiantes.models import Inscripcion
from clases.serializers import ClaseSerializer, EvaluacionSerializer, SeccionSerializer, InscripcionSerializer


@api_view(['GET', 'POST'])
def clases(request):
    if request.method == 'GET':
        serializer = ClaseSerializer(Clase.objects.all(), many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ClaseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def clase(request, id_clase):
    if request.method == 'GET':
        serializer = ClaseSerializer(Clase.objects.get(id=id_clase))
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def evaluaciones(request, id_clase):
    if request.method == 'GET':
        serializer = EvaluacionSerializer(
            Clase.objects.get(id=id_clase).evaluaciones.all(), many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = EvaluacionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'POST'])
def secciones(request, id_clase):
    if request.method == 'GET':
        serializer = SeccionSerializer(
            Clase.objects.get(id=id_clase).secciones.all(), many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SeccionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'POST'])
def inscripciones(request, id_clase, id_seccion):
    if request.method == 'GET':
        serializer = InscripcionSerializer(
            Clase.objects.get(id=id_clase).secciones.get(id=id_seccion).inscripciones.all(), many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = InscripcionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['POST'])
def actualizar_notas(request):
    body = json.loads(request.body.decode('utf-8'))
    seccion = body.get('seccion')
    inscripciones = Inscripcion.objects.filter(seccion=seccion)

    for inscripcion in inscripciones:
        print(
            f'{inscripcion.periodo.id}:{inscripcion.seccion.id}:{inscripcion.matricula.id}')

    return Response(status=200)
