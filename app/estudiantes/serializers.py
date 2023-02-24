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

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['nombre_periodo'] = f'{instance.periodo.nombre}'
        return rep
