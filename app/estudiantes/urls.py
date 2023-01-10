from django.urls import path
from . import views

app_name = 'estudiantes'
urlpatterns = [
    path('', views.estudiantes, name='estudiantes'),
    path('crear/', views.crear, name='crear'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('actualizar/<int:id>', views.actualizar, name='actualizar'),
]