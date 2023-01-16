from django.urls import path
from clases.api import views

app_name = 'api_clases'
urlpatterns = [
    path('', views.clases, name='clases'),
]
