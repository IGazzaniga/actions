from django import forms
from .models import Rutina, Cliente
from django.forms import ModelForm

class RutinaForm(forms.ModelForm):
    class Meta:
        model = Rutina
        fields = '__all__'

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'