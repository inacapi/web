from rest_framework.decorators import api_view
from rest_framework.response import Response

from clases.models import Clase
from clases.serializers import ClaseSerializer


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
