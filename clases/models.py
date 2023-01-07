from django.db import models

# Create your models here.

class Clase(models.Model):
    nombre = models.CharField(max_length=50)
    semestre = models.PositiveBigIntegerField()

    def __str__(self):
        return f'{self.nombre}'