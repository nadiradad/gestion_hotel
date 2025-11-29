from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.views.generic import CreateView, View
from django.urls import reverse_lazy
from .forms import RegistroForm

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('landing')
    
    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect('landing')

class RegistroView(CreateView):
    form_class = RegistroForm
    template_name = 'usuarios/registro.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Cuenta creada correctamente. Inicia sesión.')
        return response

    def form_invalid(self, form):
        messages.error(self.request, 'Por favor corrige los errores en el formulario.')
        return super().form_invalid(form)