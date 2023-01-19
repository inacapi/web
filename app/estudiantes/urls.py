from django.urls import path
from . import views

app_name = 'estudiantes'
urlpatterns = [
    path('', views.estudiantes, name='estudiantes'),
    path('<int:id>', views.estudiante, name='estudiante'),
    path('<int:id_estudiante>/<int:id_periodo>/<int:id_matricula>', views.secciones, name='secciones'),
]