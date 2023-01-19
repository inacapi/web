from django.urls import path
from estudiantes.api import views

urlpatterns = [
    path('', views.estudiantes),
    path('<int:id_estudiante>/matriculas/', views.matriculas, name='matriculas'),
]


