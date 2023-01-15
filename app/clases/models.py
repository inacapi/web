from django.db import models

# Create your models here.

class Clase(models.Model):
    nombre = models.CharField(max_length=50)
    semestre = models.PositiveBigIntegerField()

    def __str__(self):
        return f'{self.nombre}'

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

class Seccion(models.Model):
    id = models.PositiveBigIntegerField(primary_key=True, unique=True)
    clase = models.ForeignKey(Clase, on_delete=models.RESTRICT)
    periodo = models.ForeignKey(Periodo, on_delete=models.RESTRICT)
    docente = models.ForeignKey(Docente, on_delete=models.RESTRICT)
    
    def __str__(self):
        return f'{self.id}  {self.clase.nombre} {self.docente}'

class Evaluacion(models.Model):
    clase = models.ForeignKey(Clase, on_delete=models.RESTRICT)
    porcentaje = models.FloatField()
    numero = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.numero} - {self.porcentaje*100}% - {self.clase}'


