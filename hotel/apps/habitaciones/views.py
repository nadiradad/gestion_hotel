from django.shortcuts import render
from datetime import date
from apps.habitaciones.models import Habitacion, TipoHabitacion

# Create your views here.
def habitaciones_disponibles(request):
    fecha_entrada = request.GET.get('fecha_entrada')
    fecha_salida = request.GET.get('fecha_salida')

    habitaciones = Habitacion.objects.filter(disponible=True).select_related('tipo')

    if fecha_entrada and fecha_salida:
        # Filtramos solo las habitaciones disponibles en ese rango
        disponibles = []
        for habitacion in habitaciones:
            if habitacion.esta_disponible(fecha_entrada, fecha_salida):
                disponibles.append(habitacion)
        habitaciones = disponibles

    context = {
        'habitaciones': habitaciones,
        'fecha_entrada': fecha_entrada,
        'fecha_salida': fecha_salida,
    }
    return render(request, 'habitaciones/lista_habitaciones.html', context)
