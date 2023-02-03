from rest_framework import serializers
from clases.models import Clase, Evaluacion, Seccion
from estudiantes.models import Inscripcion


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


class InscripcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscripcion
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)

        # Quitar el perido y la sección
        del rep['periodo']
        del rep['seccion']

        # Agregar estas propiedades adicionales en la respuesta
        rep['nombre'] = f'{instance.matricula.estudiante.nombre}'
        rep['apellido'] = f'{instance.matricula.estudiante.apellido}'
        rep['notas'] = instance.notas.values('nota', 'evaluacion__numero')

        return rep
