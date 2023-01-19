from rest_framework import serializers
from clases.models import Clase, Evaluacion, Seccion


class ClaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clase
        fields = '__all__'


class EvaluacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluacion
        fields = '__all__'


class SeccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seccion
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['nombre_periodo'] = f'{instance.periodo.nombre}'
        rep['nombre_docente'] = f'{instance.docente.nombre} {instance.docente.apellido}'
        return rep
