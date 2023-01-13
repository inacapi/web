from django.contrib import admin
from estudiantes.models import Estudiante , Matricula, Inscripcion, Nota
admin.site.register([Estudiante, Matricula, Inscripcion, Nota])