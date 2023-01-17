from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from estudiantes.models import Estudiante
from estudiantes.serializers import EstudianteSerializer

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