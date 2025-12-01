from django.urls import path
from .views import ListaServiciosView

urlpatterns = [
    path('', ListaServiciosView.as_view(), name='servicios_adicionales'),
]


