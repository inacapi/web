from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Clase(models.Model):
    nombre = models.CharField(max_length=50)
    semestre = models.PositiveBigIntegerField()
    codigo = models.CharField(max_length=6, unique=True, null=True, blank=True)

    def __str__(self):
        return f'{self.nombre}'

    class Meta:
        ordering = ['semestre', 'nombre']


class Periodo(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Docente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

    class Meta:
        ordering = ['nombre', 'apellido']


class Seccion(models.Model):
    id = models.PositiveBigIntegerField(primary_key=True, unique=True)
    clase = models.ForeignKey(
        Clase, on_delete=models.RESTRICT, related_name='secciones')
    periodo = models.ForeignKey(Periodo, on_delete=models.RESTRICT)
    docente = models.ForeignKey(Docente, on_delete=models.RESTRICT)

    class Meta:
        ordering = ['clase__nombre', 'id',
                    'docente__nombre', 'docente__apellido']

    def __str__(self):
        return f'{self.id} - {self.clase.nombre} - {self.docente}'


class Evaluacion(models.Model):
    seccion = models.ForeignKey(
        Seccion, on_delete=models.RESTRICT, related_name='evaluaciones')
    porcentaje = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(1)])
    numero = models.PositiveIntegerField()
    nota_promedio = models.PositiveIntegerField(null=True, blank=True)
    fecha = models.CharField(max_length=10, null=True, blank=True)

    @property
    def porcentaje_en_porcentaje(self):
        return f'{int(self.porcentaje * 100)}%'

    class Meta:
        unique_together = ['seccion', 'numero']
        ordering = ['seccion__clase__nombre', 'numero']

    def __str__(self):
        return f'{self.numero} - {self.porcentaje*100}% - {self.seccion.clase}'
