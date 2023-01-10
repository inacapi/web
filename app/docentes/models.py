from django.db import models

# Create your models here.
class Docente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'