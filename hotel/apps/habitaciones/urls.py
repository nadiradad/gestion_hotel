from django.urls import path
from .views import HabitacionesDisponiblesView

urlpatterns = [
    path('disponibles/', HabitacionesDisponiblesView.as_view(), name='habitaciones_disponibles'),
]