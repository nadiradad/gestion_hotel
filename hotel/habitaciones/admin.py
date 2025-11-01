from django.contrib import admin
from .models import TipoHabitacion, Habitacion
from django.utils.html import format_html

# Register your models here.
@admin.register(TipoHabitacion)
class TipoHabitacionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio_por_noche', 'capacidad', 'preview_imagen')
    search_fields = ('nombre',)
    list_filter = ('capacidad',)

    def preview_imagen(self, obj):
        if obj.imagen:
            return format_html('<img src="{}" width="80" height="60" style="object-fit:cover;" />', obj.imagen.url)
        return "Sin imagen"
    preview_imagen.short_description = 'Imagen'


@admin.register(Habitacion)
class HabitacionAdmin(admin.ModelAdmin):
    list_display = ('numero', 'tipo', 'disponible')
    list_filter = ('disponible', 'tipo')
    search_fields = ('numero',)
