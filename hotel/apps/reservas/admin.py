from django.contrib import admin
from .models import Reserva

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'habitacion', 'fecha_entrada', 'fecha_salida', 'estado', 'ver_comprobante')
    list_filter = ('estado', 'fecha_entrada', 'fecha_salida')
    search_fields = ('usuario__username', 'habitacion__numero')

    # Mostrar enlace para abrir el comprobante
    def ver_comprobante(self, obj):
        if obj.comprobante:
            return f"<a href='{obj.comprobante.url}' target='_blank'>Ver comprobante</a>"
        return "Sin comprobante"
    ver_comprobante.allow_tags = True
    ver_comprobante.short_description = "Comprobante"
