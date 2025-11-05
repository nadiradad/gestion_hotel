from django.urls import path
from . import views

urlpatterns = [
    path('disponibles/', views.habitaciones_disponibles, name='habitaciones_disponibles'),
]
