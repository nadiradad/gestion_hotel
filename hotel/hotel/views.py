from django.shortcuts import render


def landing(request):
    return render(request, 'landing.html')

def perfil_usuario(request):
    return render(request, "hotel/perfil_usuario.html", {"user": request.user})