<<<<<<< HEAD
from django.shortcuts import render
=======
>>>>>>> b1da7d5f11864ef974bcfa7cf4b896b2711086f2
from django.views.generic import TemplateView

<<<<<<< HEAD
class LandingView(TemplateView):
    template_name = 'landing.html'
=======

class LandingView(TemplateView):
    template_name = 'landing.html'


def perfil_usuario(request):
    return render(request, "hotel/perfil_usuario.html", {"user": request.user})
<<<<<<< HEAD
=======
>>>>>>> 1d16ff402efcb65268be6a939a4c4502b993239e
>>>>>>> b1da7d5f11864ef974bcfa7cf4b896b2711086f2
