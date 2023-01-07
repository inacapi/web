from django.db import models

# Create your models here.
class Periodo(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre