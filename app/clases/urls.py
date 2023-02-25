from django.urls import path

from clases import views

app_name = 'clases'
urlpatterns = [
    path('', views.clases, name='clases'),
    path('<int:id_clase>/', views.clase, name='clase'),
    path('<int:id_clase>/<int:id_seccion>/',
         views.seccion, name='seccion')
]
