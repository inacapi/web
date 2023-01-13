from django.db import models
# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(primary_key=True , max_length=50)
    contrasena = models.CharField(max_length=50)

