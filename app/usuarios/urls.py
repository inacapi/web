from django.urls import path

from usuarios import views

app_name = 'usuarios'
urlpatterns = [
    path('iniciar_sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('cerrar_sesion', views.cerrar_sesion, name='cerrar_sesion'),
]
