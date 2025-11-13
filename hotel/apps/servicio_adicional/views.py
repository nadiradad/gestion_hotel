# apps/servicio_adicional/views.py
from django.shortcuts import render
from .models import ServicioAdicional

def lista_servicios(request):
    servicios = ServicioAdicional.objects.all()
    return render(request, 'servicio_adicional/servicios_adicionales.html', {'servicios': servicios})




