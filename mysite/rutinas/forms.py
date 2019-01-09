from django import forms
from .models import Rutina, Cliente, Registro
from django.forms import ModelForm

class RutinaForm(forms.ModelForm):
    class Meta:
        model = Rutina
        fields = '__all__'

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = ('peso_levantado', 'repeticiones')