from django.db import models
from clases.models import Periodo, Seccion, Evaluacion

class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'


class Matricula(models.Model):
    id = models.PositiveBigIntegerField(primary_key=True, unique=True)
    periodo = models.ForeignKey(Periodo, on_delete=models.RESTRICT)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.RESTRICT)

    def __str__(self):
        return f'{self.id}  {self.estudiante.nombre} {self.estudiante.apellido}'


class Inscripcion(models.Model):
    matricula = models.ForeignKey(Matricula, on_delete=models.RESTRICT)
    periodo = models.ForeignKey(Periodo, on_delete=models.RESTRICT)
    seccion = models.ForeignKey(Seccion, on_delete=models.RESTRICT)

    def __str__(self):
        return f'{self.matricula.estudiante} {self.seccion.clase}'


class Nota(models.Model):
    inscripcion = models.ForeignKey(Inscripcion, on_delete=models.RESTRICT)
    evaluacion = models.ForeignKey(Evaluacion, on_delete=models.RESTRICT)
    nota = models.PositiveIntegerField()


