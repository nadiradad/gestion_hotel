from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, View
from datetime import datetime
from apps.habitaciones.models import Habitacion
from apps.reservas.models import Reserva
from .forms import ComprobanteForm

class CrearReservaView(LoginRequiredMixin, CreateView):
    model = Reserva
    fields = []  # No form fields needed as we get data from POST
    template_name = 'reservas/crear_reserva.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['habitacion'] = get_object_or_404(Habitacion, id=self.kwargs['habitacion_id'])
        return context

    def form_valid(self, form):
        habitacion = get_object_or_404(Habitacion, id=self.kwargs['habitacion_id'])
        fecha_entrada = self.request.POST.get('fecha_entrada')
        fecha_salida = self.request.POST.get('fecha_salida')

        if not fecha_entrada or not fecha_salida:
            messages.error(self.request, 'Debes seleccionar las fechas.')
            return redirect('habitaciones_disponibles')

        try:
            fecha_entrada = datetime.strptime(fecha_entrada, "%Y-%m-%d").date()
            fecha_salida = datetime.strptime(fecha_salida, "%Y-%m-%d").date()
        except ValueError:
            messages.error(self.request, 'Formato de fecha inválido.')
            return redirect('habitaciones_disponibles')

        if fecha_entrada >= fecha_salida:
            messages.error(self.request, 'La fecha de salida debe ser posterior a la de entrada.')
            return redirect('habitaciones_disponibles')

        if not habitacion.esta_disponible(fecha_entrada, fecha_salida):
            messages.error(self.request, 'La habitación no está disponible en esas fechas.')
            return redirect('habitaciones_disponibles')

        reserva = form.save(commit=False)
        reserva.usuario = self.request.user
        reserva.habitacion = habitacion
        reserva.fecha_entrada = fecha_entrada
        reserva.fecha_salida = fecha_salida
        reserva.estado = 'pendiente'
        reserva.save()

        messages.success(self.request, f'Reserva creada con éxito. ID: {reserva.id}')
        return redirect('habitaciones_disponibles')

class MisReservasView(LoginRequiredMixin, ListView):
    model = Reserva
    template_name = 'reservas/mis_reservas.html'
    context_object_name = 'reservas'

    def get_queryset(self):
        return (
            self.request.user.reservas
            .select_related('habitacion', 'habitacion__tipo')
            .order_by('-fecha_entrada')
        )

class CancelarReservaView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        reserva = get_object_or_404(Reserva, id=self.kwargs['reserva_id'], usuario=request.user)
        if reserva.estado == 'cancelada':
            messages.warning(request, 'Esta reserva ya está cancelada.')
            return redirect('mis_reservas')
        return render(request, 'reservas/confirmar_cancelacion.html', {'reserva': reserva})

    def post(self, request, *args, **kwargs):
        reserva = get_object_or_404(Reserva, id=self.kwargs['reserva_id'], usuario=request.user)
        if reserva.estado != 'cancelada':
            reserva.estado = 'cancelada'
            reserva.save()
            messages.success(request, f'Reserva #{reserva.id} cancelada correctamente.')
        else:
            messages.warning(request, 'Esta reserva ya está cancelada.')
        return redirect('mis_reservas')

class SubirComprobanteView(LoginRequiredMixin, UpdateView):
    model = Reserva
    form_class = ComprobanteForm
    template_name = 'reservas/subir_comprobante.html'
    pk_url_kwarg = 'reserva_id'
    success_url = reverse_lazy('mis_reservas')

    def get_queryset(self):
        return super().get_queryset().filter(usuario=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reserva'] = self.get_object()
        return context