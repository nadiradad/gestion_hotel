from django.urls import path
from .views import (
    CrearReservaView,
    MisReservasView,
    CancelarReservaView,
    SubirComprobanteView,
)

urlpatterns = [
    path('crear/<int:habitacion_id>/', CrearReservaView.as_view(), name='crear_reserva'),
    path('mis-reservas/', MisReservasView.as_view(), name='mis_reservas'),
    path('subir_comprobante/<int:reserva_id>/', SubirComprobanteView.as_view(), name='subir_comprobante'),
]
