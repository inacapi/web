from django.urls import path
from . import views

app_name = 'usuarios'
urlpatterns = [
    path('', views.iniciar, name='iniciar'),
    path('cerrar', views.cerrar, name='cerrar'),
]