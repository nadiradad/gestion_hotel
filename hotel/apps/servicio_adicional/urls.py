# apps/servicio_adicional/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_servicios, name='servicios_adicionales'),
]


