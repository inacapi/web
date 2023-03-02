from django.db.models import Sum
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

    def validate(self, attrs):
        total = Evaluacion.objects.filter(seccion=attrs['seccion']).aggregate(
            Sum('porcentaje'))['porcentaje__sum']

        if total:
            total += attrs['porcentaje']
            if total > 1:
                raise serializers.ValidationError(
                    'El porcentaje total de las evaluaciones no puede ser mayor a 100%')
        return attrs


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

        # Agregar estas propiedades adicionales en la respuesta
        rep['clase'] = f'{instance.seccion.clase.nombre}'
        rep['docente'] = f'{instance.seccion.docente}'
        rep['nombre'] = f'{instance.matricula.estudiante.nombre}'
        rep['apellido'] = f'{instance.matricula.estudiante.apellido}'

        # Agregar las evaluaciones y notas por si no están
        # las notas, para tener el promedio y fecha
        rep['notas'] = instance.notas.values('nota')
        rep['evaluaciones'] = instance.seccion.evaluaciones.values(
            'numero', 'porcentaje', 'nota_promedio', 'fecha')

        return rep
