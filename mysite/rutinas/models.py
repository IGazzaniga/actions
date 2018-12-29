from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.core.signals import request_finished
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.


class Sucursal (models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, default='')
    domicilio = models.CharField(max_length=30, default='')
    telefono = models.BigIntegerField(default=0)

    def __str__(self):
        return '%s %s' % (self.nombre, self.domicilio)
    
class Proveedor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, default='')
    apellido = models.CharField(max_length=30, default='')
    mail = models.EmailField(max_length=254, default='')
    telefono = models.BigIntegerField(help_text="Introduzca un número de teléfono válido", default=0)

    def __str__(self):
        return self.nombre +" "+ self.apellido

class Articulo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=250)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=7, decimal_places=2)
    
    
    def __str__(self):
        return self.nombre 

class Producto(Articulo):
    stock = models.IntegerField(default=0)
    TIPOS = (
        ('Suplemento', 'Suplemento'),
        ('Máquina', 'Máquina'),
        ('Insumo', 'Insumo'),
        ('Accesorio', 'Accesorio'),
        ('Alimento', 'Alimento'),
        ('Bebida', 'Bebida'),
    )
    tipo_producto = models.CharField(
        max_length=30,
        choices=TIPOS
    )
    proveedor = models.ForeignKey(Proveedor, on_delete=models.PROTECT)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.PROTECT)
class Servicio(Articulo):
    pass

class Administrador(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30, default='')
    apellido = models.CharField(max_length=30, default='')
    sucursal = models.ForeignKey(Sucursal, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre + " " + self.apellido
class Calificacion(models.Model):
    calificacion = models.IntegerField(default=0)
    fecha = models.DateTimeField(default=now)  

class Profesor(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30, default='')
    apellido = models.CharField(max_length=30, default='')
    num_matricula = models.IntegerField(default=0)
    mail = models.EmailField(max_length=254, default='')
    telefono = models.BigIntegerField(help_text="Introduzca un número de teléfono válido", default=0)
    domicilio = models.CharField(max_length=30, default='')
    calificacion_promedio = models.DecimalField(default=0,max_digits=6, decimal_places=1)

    def __str__(self):
        return self.nombre + " " + self.apellido + ", Matrícula: "+str(self.num_matricula)
    
class Ejercicio(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, default='')
    descripcion = models.TextField(default='')
    gif = models.ImageField(default='')
    
    def __str__(self):
        return self.nombre


class Rutina(models.Model):
    id = models.AutoField(primary_key=True)
    numero = models.IntegerField(default=0)
    nombre = models.CharField(max_length=30, default='')
    
    def __str__(self):
        return self.nombre

class Dia(models.Model):
    ejercicios = models.ManyToManyField(Ejercicio)
    rutina = models.ForeignKey(Rutina, on_delete=models.CASCADE)


class Cliente(models.Model):
    """Un cliente del gimnasio"""
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30, default='')
    apellido = models.CharField(max_length=30, default='')
    foto = models.ImageField(upload_to="foto_perfil", default='')
    dni = models.IntegerField(default=0)
    mail = models.EmailField(max_length=254, default='')
    telefono = models.BigIntegerField(help_text="Introduzca un número de teléfono válido", default=0)
    domicilio = models.CharField(max_length=30, default='')
    profesor = models.ForeignKey(Profesor, on_delete=models.PROTECT)
    rutinas = models.ManyToManyField(Rutina, blank=True)

    def __str__(self):
        return self.nombre + " " + self.apellido
   
class Venta(models.Model):
    id = models.AutoField(primary_key=True)
    monto = models.DecimalField(max_digits=7, decimal_places=2)
    fecha = models.DateTimeField(default= now)
    MEDIOS = (
        ('Efectivo', 'Efectivo'),
        ('Tarjeta de crédito', 'Tarjeta de crédito'),
        ('Tarjeta de débito', 'Tarjeta de débito'),
    )
    medio_pago = models.CharField(
        max_length=30,
        choices=MEDIOS
    )
    administrador = models.ForeignKey(Administrador, on_delete=models.CASCADE)
    num_tarjeta = models.BigIntegerField(null=True, blank=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    
    def __str__(self):
        return "Venta: " + str(self.id) + ", Fecha: " + str(self.fecha) + ", Cliente: " + self.cliente.nombre +" "+self.cliente.apellido + ", Medio de pago: " + self.medio_pago

class DetalleVenta(models.Model):
    id = models.AutoField(primary_key=True)
    cantidad = models.IntegerField()
    desde = models.DateField(null=True, blank=True)
    hasta = models.DateField(null=True, blank=True)
    precio = models.DecimalField(max_digits=7, decimal_places=2)
    pago = models.ForeignKey(Venta, on_delete=models.CASCADE)
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)

class FichaMedica(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_nacimiento = models.DateField(default= now)
    altura = models.IntegerField(help_text="Ingrese la altura en centímetros")
    peso = models.IntegerField(help_text="Ingrese el peso en kg")
    SEXO = (
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino'),
    )
    sexo = models.CharField(
        max_length=20,
        choices=SEXO
    )
    mutual = models.CharField(max_length=30, default='')
    observaciones = models.TextField(default='')
    telefono_emergencia = models.BigIntegerField(help_text="Introduzca un número de teléfono válido", default=0)
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE)

    
class RutinaCliente(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    rutina = models.ForeignKey(Rutina, on_delete=models.PROTECT)
    actual = models.BooleanField()

class RutinaEjercicio(models.Model):
    ejercicio = models.ForeignKey(Ejercicio, on_delete=models.PROTECT)
    rutina = models.ForeignKey(Rutina, on_delete=models.PROTECT)
    dia = models.ForeignKey(Dia, on_delete=models.PROTECT)

class Registro(models.Model):
    id = models.AutoField(primary_key=True)
    peso_levantado = models.IntegerField(default=0)
    repeticiones = models.IntegerField(default=0)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    rutina = models.ForeignKey(Rutina, on_delete=models.PROTECT)
    ejercicio = models.ForeignKey(Ejercicio, on_delete=models.PROTECT)
    completado = models.BooleanField(default=False)

class DiaEjercicio(models.Model):
    dia = models.ForeignKey(Dia, on_delete=models.PROTECT)
    ejercicio = models.ForeignKey(Ejercicio, on_delete=models.PROTECT)