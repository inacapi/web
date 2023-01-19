from rest_framework import serializers
from estudiantes.models import Estudiante, Matricula


class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante 
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = '__all__'