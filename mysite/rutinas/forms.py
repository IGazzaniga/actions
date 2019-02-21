from django import forms
from .models import Rutina, Semana, Profesor, Cliente, RutinaCliente, Venta, DetalleVenta, FichaMedica, Registro, Dia, Ejercicio, Serie
from django.forms import ModelForm, inlineformset_factory
from django.utils.translation import ugettext_lazy as _
from mysite import settings

class RutinaClienteForm(forms.ModelForm):
    rutina = forms.ModelChoiceField(queryset=Rutina.objects.all())
    class Meta:
        model = RutinaCliente
        fields = ['cliente', 'rutina']
        labels = {
            'Cliente': _('Cliente'),
            'rutina': _('Rutina'),
        }

class RutinaForm(forms.ModelForm):
    class Meta:
        model = Rutina
        fields = '__all__'
        labels = {
            'nombre': _('Nombre')
        }

class DiaForm(forms.ModelForm):
    ejercicios = forms.ModelMultipleChoiceField(
        queryset=Ejercicio.objects.all(), 
        widget=forms.CheckboxSelectMultiple,
    )
    class Meta:
        model = Dia
        fields = ['ejercicios']
        labels = {
            'ejercicios': _('Ejercicios')
        }

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre','apellido','foto', 'dni', 'mail', 'telefono', 'domicilio']
        labels = {
            'nombre': _('Nombre'),
            'apellido': _('Apellido'),
            'foto': _('Foto de perfil'),
            'dni': _('DNI'),
            'mail': _('E-mail'),
            'telefono': _('Teléfono'),
            'domicilio': _('Domicilio')
        }
        widgets = {
            'nombre': forms.TextInput(),
            'apellido': forms.TextInput(),
            'foto': forms.widgets.ClearableFileInput(),
            'dni': forms.NumberInput(),
            'mail': forms.EmailInput(),
            'telefono': forms.NumberInput(),
            'domicilio': forms.TextInput()
        }
    
    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        self.fields['foto'].null = True

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre','apellido','foto','mail', 'telefono', 'domicilio']
        labels = {
            'nombre': _('Nombre'),
            'apellido': _('Apellido'),
            'foto': _('Foto de perfil'),
            'mail': _('E-mail'),
            'telefono': _('Teléfono'),
            'domicilio': _('Domicilio')
        }
        widgets = {
            'nombre': forms.TextInput(),
            'apellido': forms.TextInput(),
            'foto': forms.widgets.ClearableFileInput(),
            'mail': forms.EmailInput(),
            'telefono': forms.NumberInput(),
            'domicilio': forms.TextInput()
        }
    
    def __init__(self, *args, **kwargs):
        super(ProfesorForm, self).__init__(*args, **kwargs)
        self.fields['foto'].null = True

class FichaForm(forms.ModelForm):
    class Meta:
        model = FichaMedica
        fields = ('altura', 'peso', 'sexo', 'mutual', 'observaciones', 'telefono_emergencia')
        labels = {'altura': _('Altura'),
            'peso': _('Peso'),
            'sexo': _('Sexo'),
            'mutual': _('Mutual'),
            'observaciones': _('Observaciones'),
            'telefono_emergencia':  _('Teléfono de emergencia')
        }
        widgets = {
            'altura': forms.NumberInput(),
            'peso': forms.NumberInput(),
            'sexo': forms.widgets.Select(),
            'mutual': forms.TextInput(),
            'observaciones': forms.Textarea(),
            'telefono_emergencia': forms.NumberInput()
        }

    def __init__(self, *args, **kwargs):
        super(FichaForm, self).__init__(*args, **kwargs)
        self.fields['sexo'].choices = (FichaMedica.SEXO[0], FichaMedica.SEXO[1])

    
class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['medio_pago', 'num_tarjeta']
        labels = {
            'medio_pago': _('Medio de pago'),
            'num_tarjeta': _('Número de tarjeta')
        }
        widgets = {
            'medio_pago': forms.Select(),
            'num_tarjeta': forms.NumberInput()
        }
    
    def __init__(self, *args, **kwargs):
        super(VentaForm, self).__init__(*args, **kwargs)
        self.fields['medio_pago'].choices = (Venta.MEDIOS[1], Venta.MEDIOS[2])
        self.fields['num_tarjeta'].required = True

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = ['completado']
        labels = {
            'completado': _('¡Terminé!')
        }
        
class SerieForm(forms.ModelForm):
    class Meta:
        model = Serie
        fields = ['numero', 'repeticiones', 'peso_levantado']
