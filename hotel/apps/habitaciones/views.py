from django.views.generic import ListView
from datetime import date
from .models import Habitacion

class HabitacionesDisponiblesView(ListView):
    model = Habitacion
    template_name = 'habitaciones/lista_habitaciones.html'
    context_object_name = 'habitaciones'

    def get_queryset(self):
        queryset = super().get_queryset().filter(disponible=True).select_related('tipo')
        fecha_entrada = self.request.GET.get('fecha_entrada')
        fecha_salida = self.request.GET.get('fecha_salida')

        if fecha_entrada and fecha_salida:
            disponibles = []
            for habitacion in queryset:
                if habitacion.esta_disponible(fecha_entrada, fecha_salida):
                    disponibles.append(habitacion)
            return disponibles
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fecha_entrada'] = self.request.GET.get('fecha_entrada')
        context['fecha_salida'] = self.request.GET.get('fecha_salida')
        return context