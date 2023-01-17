from django.urls import path
from estudiantes.api import views

urlpatterns = [
    path('', views.estudiantes),
]


