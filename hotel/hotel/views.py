from django.views.generic import TemplateView

<<<<<<< HEAD
class LandingView(TemplateView):
    template_name = 'landing.html'
=======

def landing(request):
    return render(request, 'landing.html')

def perfil_usuario(request):
    return render(request, "hotel/perfil_usuario.html", {"user": request.user})
>>>>>>> 1d16ff402efcb65268be6a939a4c4502b993239e
