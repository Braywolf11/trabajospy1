from django.urls import path, include
from apps.mascotas.views import index_mascota


urlpatterns = [
    path(r'',index_mascota),
]
