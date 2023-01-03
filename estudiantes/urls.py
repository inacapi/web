from django.urls import path
from .views import index, crear
urlpatterns = [
    path('', index, name='admin-index'),
    path('crear/', crear, name='admin-crear'),
]