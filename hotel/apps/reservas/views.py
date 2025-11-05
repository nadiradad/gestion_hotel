from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime
from apps.habitaciones.models import Habitacion
from apps.reservas.models import Reserva

# Create your views here.
@login_required
def crear_reserva(request, habitacion_id):
    habitacion = get_object_or_404(Habitacion, id=habitacion_id)

    if request.method == 'POST':
        fecha_entrada = request.POST.get('fecha_entrada')
        fecha_salida = request.POST.get('fecha_salida')

        # Validaciones básicas
        if not fecha_entrada or not fecha_salida:
            messages.error(request, 'Debes seleccionar las fechas.')
            return redirect('habitaciones_disponibles')

        fecha_entrada = datetime.strptime(fecha_entrada, "%Y-%m-%d").date()
        fecha_salida = datetime.strptime(fecha_salida, "%Y-%m-%d").date()

        if fecha_entrada >= fecha_salida:
            messages.error(request, 'La fecha de salida debe ser posterior a la de entrada.')
            return redirect('habitaciones_disponibles')

        if not habitacion.esta_disponible(fecha_entrada, fecha_salida):
            messages.error(request, 'La habitación no está disponible en esas fechas.')
            return redirect('habitaciones_disponibles')

        # Crear la reserva
        reserva = Reserva.objects.create(
            usuario=request.user,
            habitacion=habitacion,
            fecha_entrada=fecha_entrada,
            fecha_salida=fecha_salida,
            estado='pendiente'
        )

        messages.success(request, f'Reserva creada con éxito. ID: {reserva.id}')
        return redirect('habitaciones_disponibles')

    context = {'habitacion': habitacion}
    return render(request, 'reservas/crear_reserva.html', context)

@login_required
def mis_reservas(request):
    reservas = (
        request.user.reservas
        .select_related('habitacion', 'habitacion__tipo')
        .order_by('-fecha_entrada')
    )
    return render(request, 'reservas/mis_reservas.html', {'reservas': reservas})

@login_required
def cancelar_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id, usuario=request.user)

    if reserva.estado == 'cancelada':
        messages.warning(request, 'Esta reserva ya está cancelada.')
        return redirect('mis_reservas')

    if request.method == 'POST':
        reserva.estado = 'cancelada'
        reserva.save()
        messages.success(request, f'Reserva #{reserva.id} cancelada correctamente.')
        return redirect('mis_reservas')

    # Si entra por GET, pedimos confirmación
    return render(request, 'reservas/confirmar_cancelacion.html', {'reserva': reserva})

