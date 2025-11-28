# apps/servicio_adicional/views.py
from django.views.generic import ListView
from .models import ServicioAdicional

class ListaServiciosView(ListView):
    model = ServicioAdicional
    template_name = 'servicio_adicional/servicios_adicionales.html'
    context_object_name = 'servicios'





