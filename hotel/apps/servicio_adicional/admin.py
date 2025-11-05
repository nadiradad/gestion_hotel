from django.contrib import admin
from .models import ServicioAdicional, ReservaServicio

# Register your models here.
@admin.register(ServicioAdicional)
class ServicioAdicionalAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio')
    search_fields = ('nombre',)

@admin.register(ReservaServicio)
class ReservaServicioAdmin(admin.ModelAdmin):
    list_display = ('reserva', 'servicio', 'cantidad', 'total_precio', 'fecha_reserva')
    search_fields = ('reserva__usuario__username', 'servicio__nombre')
