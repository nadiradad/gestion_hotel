from django.db import models
from datetime import date

# Create your models here.
class TipoHabitacion(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    precio_por_noche = models.DecimalField(max_digits=8, decimal_places=2)
    capacidad = models.PositiveIntegerField(default=1)
    imagen = models.ImageField(upload_to='habitaciones/', blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - ${self.precio_por_noche}/noche"

class Habitacion(models.Model):
    numero = models.CharField(max_length=10, unique=True)
    tipo = models.ForeignKey('TipoHabitacion', on_delete=models.CASCADE, related_name='habitaciones')
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"Habitación {self.numero} ({self.tipo.nombre})"

    def esta_disponible(self, fecha_entrada, fecha_salida):
        """Retorna True si la habitación no tiene reservas en el rango dado."""
        reservas = self.reservas.filter(
            estado__in=['pendiente', 'confirmada'],
            fecha_entrada__lt=fecha_salida,
            fecha_salida__gt=fecha_entrada
        )
        return not reservas.exists()
