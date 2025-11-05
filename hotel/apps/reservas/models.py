from django.db import models
from django.conf import settings
from apps.habitaciones.models import Habitacion

# Create your models here.
class Reserva(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reservas')
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE, related_name='reservas')
    fecha_entrada = models.DateField()
    fecha_salida = models.DateField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado_choices = [
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada'),
        ('finalizada', 'Finalizada'),
    ]
    estado = models.CharField(max_length=20, choices=estado_choices, default='pendiente')

    def __str__(self):
        return f"Reserva {self.id} - {self.usuario.username} ({self.estado})"

    def total_noches(self):
        return (self.fecha_salida - self.fecha_entrada).days

    def total_precio(self):
        return self.total_noches() * self.habitacion.tipo.precio_por_noche
