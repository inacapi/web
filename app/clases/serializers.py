from rest_framework import serializers
from clases.models import Clase


class ClaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clase
        fields = '__all__'
