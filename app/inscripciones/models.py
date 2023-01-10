from django.db import models
from matriculas.models import Matricula
from secciones.models import Seccion
from periodos.models import Periodo 

class Inscripcion(models.Model):
    matricula = models.ForeignKey(Matricula, on_delete=models.RESTRICT)
    periodo = models.ForeignKey(Periodo, on_delete=models.RESTRICT)
    seccion = models.ForeignKey(Seccion, on_delete=models.RESTRICT)

    def __str__(self):
        return f'{self.matricula.estudiante} {self.seccion.clase}'