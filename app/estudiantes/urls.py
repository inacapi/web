from django.urls import path

from estudiantes import views

app_name = 'estudiantes'
urlpatterns = [
    path('', views.estudiantes, name='estudiantes'),
    path('<int:id>/', views.estudiante, name='estudiante'),
    path('<int:id_estudiante>/<int:id_matricula>/',
         views.matricula, name='matricula')
]
