import json
import os
import requests

from rest_framework.decorators import api_view
from rest_framework.response import Response

from clases.models import Clase, Evaluacion, Seccion
from estudiantes.models import Inscripcion, Nota, Estudiante
from clases.serializers import ClaseSerializer, EvaluacionSerializer, SeccionSerializer, InscripcionSerializer
from estudiantes.serializers import EstudianteSerializer, MatriculaSerializer


USERNAME = os.environ.get('USERNAME')
PASSWORD = os.environ.get('PASSWORD')


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


@api_view(['GET', 'POST'])
def evaluaciones(request):
    if request.method == 'GET':
        clase = request.GET.get('clase')
        serializer = EvaluacionSerializer(
            Evaluacion.objects.filter(clase=clase), many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = EvaluacionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'POST'])
def secciones(request):
    if request.method == 'GET':
        clase = request.GET.get('clase')
        serializer = SeccionSerializer(
            Seccion.objects.filter(clase=clase), many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SeccionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@ api_view(['GET', 'POST'])
def inscripciones(request):
    if request.method == 'GET':
        seccion = request.GET.get('seccion')
        matricula = request.GET.get('matricula')

        if seccion:
            inscripciones = Inscripcion.objects.filter(seccion=seccion)
        elif matricula:
            inscripciones = Inscripcion.objects.filter(matricula=matricula)

        serializer = InscripcionSerializer(inscripciones, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = InscripcionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@ api_view(['POST'])
def actualizar_notas(request):
    body = json.loads(request.body.decode('utf-8'))
    seccion = body.get('seccion')
    inscripciones = Inscripcion.objects.filter(seccion=seccion)

    token = request.session.get('token_inacap', 'obtener_token')
    actualizar_token = False

    for inscripcion in inscripciones:
        headers = {'Authorization': token}
        data = {
            'periodo': inscripcion.periodo.id,
            'seccion': inscripcion.seccion.id,
            'matricula': inscripcion.matricula.id
        }

        response = requests.post(
            'http://api:3000/seccion', headers=headers, json=data)

        if response.status_code == 401:
            actualizar_token = True
            break

        evaluaciones = response.json()['data']['notas']
        if len(evaluaciones) == 0:
            print('No hay evaluaciones aún')
            return Response(data={'mensaje_error': 'No hay evaluaciones aún.'}, status=400)

        for evaluacion in evaluaciones:
            porcentaje = evaluacion['caliNponderacion']
            clase = inscripcion.seccion.clase.id
            numero = evaluacion['caliNevaluacion']
            porcentaje = float(porcentaje[:porcentaje.find('%')]) / 100

            evaluacion_bd = Evaluacion.objects.get(
                clase=clase, numero=numero, porcentaje=porcentaje)

            try:
                nota = float(evaluacion['calaNnota']) * 10
            except ValueError:
                continue  # Esa evaluación no tiene nota todavía

            Nota.objects.update_or_create(
                inscripcion=inscripcion, evaluacion=evaluacion_bd, nota=nota)

    if actualizar_token:
        response = requests.post('http://api:3000/obtener_token', json={
            'nombre': USERNAME,
            'contraseña': PASSWORD
        })
        request.session['token_inacap'] = response.json()['token']
        return Response(data={'mensaje_error': 'Token renovado, intentar nuevamente.'}, status=400)

    return Response(status=200)


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
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'POST'])
def matriculas(request):
    if request.method == 'GET':
        estudiante = request.GET.get('estudiante')
        matriculas = Estudiante.objects.get(id=estudiante).matriculas.all()
        serializer = MatriculaSerializer(matriculas, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MatriculaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
