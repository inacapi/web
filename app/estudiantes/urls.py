from django.urls import path
from . import views

app_name = 'estudiantes'
urlpatterns = [
    path('', views.estudiantes, name='estudiantes'),
    path('detalle_estudiante/<int:id>', views.detalle_estudiante, name='detalle_estudiante'),
    path('seccion_estudiante/<int:id>/<int:matricula>', views.seccion_estudiante, name='seccion_estudiante'),
]