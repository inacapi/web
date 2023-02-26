from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('estudiantes.urls')),
    path('api/estudiantes/', include('estudiantes.api.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('clases/', include('clases.urls')),
    path('api/', include('api.urls'))
]
