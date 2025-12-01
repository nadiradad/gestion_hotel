from django.shortcuts import render
from django.views.generic import TemplateView


class LandingView(TemplateView):
    template_name = 'landing.html'


def perfil_usuario(request):
    return render(request, "hotel/perfil_usuario.html", {"user": request.user})
