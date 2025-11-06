from django.db import models
from apps.reservas.models import Reserva

# Create your models here.
class ServicioAdicional(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.nombre} (${self.precio})"


class ReservaServicio(models.Model):
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE, related_name='servicios')
    servicio = models.ForeignKey(ServicioAdicional, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    

    def __str__(self):
        return f"{self.servicio.nombre} x{self.cantidad} (Reserva {self.reserva.id})"

    def total_precio(self):
        return self.cantidad * self.servicio.precio
