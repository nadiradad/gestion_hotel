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
    path('cancelar/<int:reserva_id>/', CancelarReservaView.as_view(), name='cancelar_reserva'),
<<<<<<< HEAD
    path('subir_comprobante/<int:reserva_id>/', SubirComprobanteView.as_view(), name='subir_comprobante'),
]
=======
    path('subir_comprobante/<int:pk>/', SubirComprobanteView.as_view(), name='subir_comprobante'),
]
>>>>>>> 1d16ff402efcb65268be6a939a4c4502b993239e
