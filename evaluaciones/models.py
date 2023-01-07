from django.db import models
from clases.models import Clase

# Create your models here.
class Evaluacion(models.Model):
    clase = models.ForeignKey(Clase, on_delete=models.RESTRICT)
    porcentaje = models.FloatField()
    numero = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.numero} - {self.porcentaje*100}% - {self.clase}'