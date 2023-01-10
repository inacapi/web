from django.db import models
from evaluaciones.models import Evaluacion
from inscripciones.models import Inscripcion
# Create your models here.

class Nota(models.Model):
    inscripcion = models.ForeignKey(Inscripcion, on_delete=models.RESTRICT)
    evaluacion = models.ForeignKey(Evaluacion, on_delete=models.RESTRICT)
    nota = models.PositiveIntegerField()