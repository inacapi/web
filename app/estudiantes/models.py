from django.db import models

from clases.models import Evaluacion, Periodo, Seccion


class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)

    class Meta:
        ordering = ['nombre', '-apellido']

    def __str__(self):
        return f'{self.nombre} {self.apellido}'


class Matricula(models.Model):
    id = models.PositiveBigIntegerField(primary_key=True, unique=True)
    periodo = models.ForeignKey(Periodo, on_delete=models.RESTRICT)
    estudiante = models.ForeignKey(
        Estudiante, on_delete=models.RESTRICT, related_name='matriculas')

    class Meta:
        unique_together = ['periodo', 'estudiante']
        ordering = ['periodo', 'estudiante__nombre', 'estudiante__apellido']

    def __str__(self):
        return f'{self.estudiante}'


class Inscripcion(models.Model):
    matricula = models.ForeignKey(
        Matricula, on_delete=models.RESTRICT, related_name='inscripciones')
    periodo = models.ForeignKey(Periodo, on_delete=models.RESTRICT)
    seccion = models.ForeignKey(
        Seccion, on_delete=models.RESTRICT, related_name='inscripciones')
    nota_presentacion = models.CharField(max_length=5, blank=True, null=True)
    nota_final = models.CharField(max_length=5, blank=True, null=True)
    asistencia = models.CharField(max_length=5, blank=True, null=True)
    situacion = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f'{self.matricula.estudiante} {self.seccion.clase}'

    class Meta:
        ordering = ['matricula__estudiante__nombre',
                    '-matricula__estudiante__apellido', 'seccion__clase__nombre']
        unique_together = ['matricula', 'seccion', 'periodo']


class Nota(models.Model):
    inscripcion = models.ForeignKey(
        Inscripcion, on_delete=models.RESTRICT, related_name='notas')
    evaluacion = models.ForeignKey(Evaluacion, on_delete=models.RESTRICT)
    nota = models.PositiveIntegerField()

    class Meta:
        unique_together = ['inscripcion', 'evaluacion']
        ordering = ['evaluacion__numero']
