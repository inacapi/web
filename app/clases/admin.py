from django.contrib import admin
from clases.models import Clase, Periodo, Docente, Seccion, Evaluacion
admin.site.register([Clase, Periodo, Docente, Seccion, Evaluacion])
