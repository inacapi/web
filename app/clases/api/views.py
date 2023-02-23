import json
import os
import requests

from rest_framework.decorators import api_view
from rest_framework.response import Response

from clases.models import Clase, Evaluacion
from estudiantes.models import Inscripcion, Nota
from clases.serializers import ClaseSerializer, EvaluacionSerializer, SeccionSerializer, InscripcionSerializer


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
