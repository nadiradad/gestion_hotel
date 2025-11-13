from django.urls import path
from . import views

urlpatterns = [
    path('crear/<int:habitacion_id>/', views.crear_reserva, name='crear_reserva'),
    path('mis-reservas/', views.mis_reservas, name='mis_reservas'),
    path('cancelar/<int:reserva_id>/', views.cancelar_reserva, name='cancelar_reserva'),
    path('subir_comprobante/<int:reserva_id>/', views.subir_comprobante, name='subir_comprobante'),
]
