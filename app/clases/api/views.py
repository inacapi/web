from rest_framework.decorators import api_view
from rest_framework.response import Response

from clases.models import Clase
from clases.serializers import ClaseSerializer


@api_view(['GET'])
def clases(request):
    serializer = ClaseSerializer(Clase.objects.all(), many=True)
    return Response(serializer.data)
