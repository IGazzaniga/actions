from django import forms
from .models import Rutina, Cliente, Venta, DetalleVenta
from django.forms import ModelForm

class RutinaForm(forms.ModelForm):
    class Meta:
        model = Rutina
        fields = '__all__'

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['medio_pago', 'num_tarjeta']

class DetalleVentaForm(forms.ModelForm):
    class Meta:
        model = DetalleVenta
        fields = ['cantidad', 'articulo']