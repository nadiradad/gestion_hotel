from django import forms
from .models import Reserva

class ComprobanteForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['comprobante']
