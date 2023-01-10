from django.db import models
from docentes.models import Docente
from clases.models import Clase
from periodos.models import Periodo 
# Create your models here.
class Seccion(models.Model):
    id = models.PositiveBigIntegerField(primary_key=True, unique=True)
    clase = models.ForeignKey(Clase, on_delete=models.RESTRICT)
    periodo = models.ForeignKey(Periodo, on_delete=models.RESTRICT)
    docente = models.ForeignKey(Docente, on_delete=models.RESTRICT)

     
    def __str__(self):
        return f'{self.id}  {self.clase.nombre}'