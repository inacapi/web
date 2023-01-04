from django.db import models
from estudiantes.models import Estudiante
from periodos.models import Periodo 
# Create your models here.
class Matricula(models.Model):
    id = models.PositiveBigIntegerField(primary_key=True, unique=True)
    periodo = models.ForeignKey(Periodo, on_delete=models.RESTRICT)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.RESTRICT)