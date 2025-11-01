from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistroForm  # <- Importar tu formulario personalizado

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)  # <- Usar RegistroForm, NO UserCreationForm
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Cuenta creada correctamente. Inicia sesión.')
            return redirect('login')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = RegistroForm()

    return render(request, 'usuarios/registro.html', {'form': form})
