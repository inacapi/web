from django.db import models

# Create your models here.
class Periodo(models.Model):
    nombre = models.CharField(max_length=50)