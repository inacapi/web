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
        seccion = request.GET.get('seccion')
        serializer = EvaluacionSerializer(
            Evaluacion.objects.filter(seccion=seccion), many=True)
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


@api_view(['GET', 'POST'])
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


@api_view(['POST'])
def actualizar_notas(request):
    body = json.loads(request.body.decode('utf-8'))
    seccion = body.get('seccion')
    matricula = body.get('matricula')

    if seccion:
        inscripciones = Inscripcion.objects.filter(seccion=seccion)
        matricula = [inscripcion.matricula.id for inscripcion in inscripciones]

    elif matricula:
        inscripciones = Inscripcion.objects.filter(matricula=matricula)
        seccion = [inscripcion.seccion.id for inscripcion in inscripciones]

    if len(inscripciones) == 0:
        return Response(data={'mensaje_error': 'No hay inscripciones con esa matrícula o sección.'}, status=400)

    periodo = inscripciones[0].periodo.id

    token = request.session.get('token_inacap', 'obtener_token')
    actualizar_token = False

    headers = {'Authorization': token}
    body = {
        'periodo': periodo,
        'matricula': matricula,
        'seccion': seccion,
    }

    datos = requests.post(
        'http://api:3000/seccion', headers=headers, json=body)

    paquetes = list(zip(inscripciones, datos.json()))

    for paquete in paquetes:
        if 'status' in paquete[1] and paquete[1]['status'] == 401:
            actualizar_token = True
            break

        evaluaciones = paquete[1]['notas']
        if len(evaluaciones) == 0:
            continue  # Hay un error con la matrícula o sección

        for evaluacion in evaluaciones:
            porcentaje = evaluacion['caliNponderacion']
            # No uso seccion porque puede ser una lista cuando se envía una matrícula
            id_seccion = paquete[0].seccion.id
            numero = evaluacion['caliNevaluacion']
            porcentaje = float(porcentaje[:porcentaje.find('%')]) / 100

            try:
                evaluacion_bd = Evaluacion.objects.get(
                    seccion=id_seccion, numero=numero, porcentaje=porcentaje)
            except Evaluacion.DoesNotExist:
                break  # Faltan las evaluaciones de esa clase

            try:
                nota = float(evaluacion['calaNnota']) * 10
            except ValueError:
                continue  # Esa evaluación no tiene nota todavía

            Nota.objects.update_or_create(
                inscripcion=paquete[0], evaluacion=evaluacion_bd, defaults={'nota': nota})

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
