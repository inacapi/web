from django.urls import path
from clases.api import views

app_name = 'api_clases'
urlpatterns = [
    path('', views.clases, name='clases'),
    path('<int:id_clase>/', views.clase, name='clase'),
    path('<int:id_clase>/evaluaciones/',
         views.evaluaciones, name='evaluaciones'),
    path('<int:id_clase>/secciones/', views.secciones, name='secciones'),
    path('<int:id_clase>/<int:id_seccion>/inscripciones/',
         views.inscripciones, name='inscripciones'),
    path('actualizar_notas/',
         views.actualizar_notas, name='actualizar_notas')
]
