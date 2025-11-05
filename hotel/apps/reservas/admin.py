from django.contrib import admin
from .models import Reserva

# Register your models here.
@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'habitacion', 'fecha_entrada', 'fecha_salida', 'estado')
    list_filter = ('estado', 'fecha_entrada', 'fecha_salida')
    search_fields = ('usuario__username', 'habitacion__numero')
    date_hierarchy = 'fecha_entrada'
