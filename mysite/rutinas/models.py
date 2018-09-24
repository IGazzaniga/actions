from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.


class Inventario (models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, default='')

class Sucursal (models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, default='')
    domicilio = models.CharField(max_length=30, default='')
    telefono = models.BigIntegerField(default=0)
    inventario = models.OneToOneField(Inventario, on_delete=models.PROTECT)
    
    
class Proveedor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, default='')
    apellido = models.CharField(max_length=30, default='')
    mail = models.EmailField(max_length=254, default='')
    telefono = models.BigIntegerField(default=0)

class Producto (models.Model):
    id = models.AutoField(primary_key=True)
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
    nombre = models.CharField(max_length=200, default='')
    proveedor = models.ForeignKey(Proveedor, on_delete=models.PROTECT)
    inventario = models.ForeignKey(Inventario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Administrador(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30, default='')
    apellido = models.CharField(max_length=30, default='')
    sucursal = models.ForeignKey(Sucursal, on_delete=models.PROTECT)


class Profesor(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30, default='')
    apellido = models.CharField(max_length=30, default='')
    num_matricula = models.IntegerField(default=0)
    mail = models.EmailField(max_length=254, default='')
    telefono = models.BigIntegerField(default=0)
    domicilio = models.CharField(max_length=30, default='')

class Rutina(models.Model):
    id = models.AutoField(primary_key=True)
    SESIONES = (
        ('3 días', '3 días'),
        ('5 días', '5 días'),
    )
    sesiones = models.CharField(
        max_length=20,
        choices=SESIONES
    )

    def __str__(self):
        return self.id

class Ejercicio(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, default='')
    gif = models.ImageField
    TRENES = (
        ('Tren superior', 'Tren superior'),
        ('Tren inferior', 'Tren inferior'),
    )
    tren = models.CharField(
        max_length=20,
        choices=TRENES
    )

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    """Un cliente del gimnasio"""
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30, default='')
    apellido = models.CharField(max_length=30, default='')
    dni = models.IntegerField(default=0)
    mail = models.EmailField(max_length=254, default='')
    telefono = models.BigIntegerField(default=0)
    domicilio = models.CharField(max_length=30, default='')
    profesor = models.ForeignKey(Profesor, on_delete=models.PROTECT)
    rutinas = models.ManyToManyField(Rutina)


class Pago(models.Model):
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
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

        
class FichaMedica(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_nacimiento = models.DateField(default= now)
    altura = models.IntegerField()
    peso = models.DecimalField(max_digits=5, decimal_places=2)
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
    telefono_emergencia = models.BigIntegerField(default=0)
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.cliente

class RutinaCliente(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    rutina = models.ForeignKey(Rutina, on_delete=models.PROTECT)


class RutinaEjercicio(models.Model):
    ejercicio = models.ForeignKey(Ejercicio, on_delete=models.PROTECT)
    rutina = models.ForeignKey(Rutina, on_delete=models.PROTECT)

class Registro(models.Model):
    id = models.AutoField(primary_key=True)
    peso_levantado = models.IntegerField(default=0)
    repeticiones = models.IntegerField(default=0)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    rutina = models.ForeignKey(Rutina, on_delete=models.PROTECT)
    ejercicio = models.ForeignKey(Ejercicio, on_delete=models.PROTECT)
