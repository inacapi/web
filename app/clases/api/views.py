from rest_framework.decorators import api_view
from rest_framework.response import Response

from clases.models import Clase
from clases.serializers import ClaseSerializer, EvaluacionSerializer, SeccionSerializer


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
