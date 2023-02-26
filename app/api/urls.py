from django.urls import path
from api import views

urlpatterns = [
    path('clases', views.clases, name='clases'),
    path('evaluaciones', views.evaluaciones, name='evaluaciones'),
    path('secciones', views.secciones, name='secciones'),
    path('inscripciones', views.inscripciones, name='inscripciones'),
    path('actualizar_notas', views.actualizar_notas, name='actualizar_notas')
]
