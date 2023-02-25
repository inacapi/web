from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from clases.serializers import InscripcionSerializer
from estudiantes.models import Estudiante
from estudiantes.serializers import EstudianteSerializer, MatriculaSerializer


@api_view(['GET', 'POST'])
def estudiantes(request):
    if request.method == 'GET':
        estudiantes = Estudiante.objects.all()
        serializer = EstudianteSerializer(estudiantes, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = EstudianteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def matriculas(request, id_estudiante):
    if request.method == 'GET':
        matriculas = Estudiante.objects.get(id=id_estudiante).matriculas.all()
        serializer = MatriculaSerializer(matriculas, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MatriculaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def inscripciones(request, id_estudiante, id_matricula):
    if request.method == 'GET':
        serializer = InscripcionSerializer(Estudiante.objects.get(
            id=id_estudiante).matriculas.get(id=id_matricula).inscripciones.all(), many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = InscripcionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
