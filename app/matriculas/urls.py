from django.urls import path
from . import views

app_name = 'matriculas'
urlpatterns = [
    path('', views.matriculas, name='matriculas'),
    path('crear/', views.crear, name='crear'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('actualizar/<int:id>', views.actualizar, name='actualizar'),
]