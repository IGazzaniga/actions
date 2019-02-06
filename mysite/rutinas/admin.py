from django.contrib import admin
from .models import (Articulo, Proveedor, Sucursal, Producto, 
Administrador, Profesor, Rutina, Dia, RutinaEjercicio, Ejercicio, Cliente, Venta, FichaMedica, DetalleVenta, Servicio, Registro, RutinaCliente, Serie)


class AdministradorAdmin(admin.ModelAdmin):
    fields = ['user','nombre', 'apellido', 'sucursal']
admin.site.register(Administrador, AdministradorAdmin)

class SucursalAdmin(admin.ModelAdmin):
    fields = ['nombre', 'domicilio', 'telefono']
admin.site.register(Sucursal, SucursalAdmin)

class ProveedorAdmin(admin.ModelAdmin):
    fields = ['nombre', 'apellido', 'mail','telefono']

admin.site.register(Proveedor, ProveedorAdmin)

class ArticuloAdmin(admin.ModelAdmin):
    model = Articulo
admin.site.register(Articulo, ArticuloAdmin)

class ProductoAdmin(admin.ModelAdmin):
    fields = ['nombre','descripcion','precio','tipo_producto', 'proveedor', 'sucursal', 'stock', 'imagen']
admin.site.register(Producto, ProductoAdmin)

class ServicioAdmin(admin.ModelAdmin):
    fields = ['nombre','descripcion','precio', 'imagen']
admin.site.register(Servicio, ServicioAdmin)

class ProfesorAdmin(admin.ModelAdmin):
    fields = ['user', 'nombre', 'apellido', 'num_matricula', 'mail', 'telefono', 'domicilio', 'foto']
admin.site.register(Profesor, ProfesorAdmin)

class EjercicioAdmin(admin.ModelAdmin):
    fields = ['nombre', 'descripcion', 'gif']
admin.site.register(Ejercicio, EjercicioAdmin)

class DiaInline(admin.TabularInline):
    model = Dia
    fields = ['ejercicios']
    extra = 0
    min_num = 3

class RutinaAdmin(admin.ModelAdmin):
    fields = ['numero', 'nombre']
    inlines = [DiaInline] 
admin.site.register(Rutina, RutinaAdmin)

class FichaMedicaInline(admin.TabularInline):
    model = FichaMedica
    fields = ['fecha_nacimiento', 'altura', 'peso', 'sexo', 'mutual', 'observaciones', 'telefono_emergencia']

class RutinaInline(admin.TabularInline):
    model = Cliente.rutinas.through

class ClienteAdmin(admin.ModelAdmin):
    fields = ['user', 'nombre', 'apellido', 'dni', 'foto', 'mail', 'telefono', 'domicilio', 'profesor']
    inlines = [FichaMedicaInline, RutinaInline]

admin.site.register(Cliente, ClienteAdmin)

class DetalleVentaInline(admin.TabularInline):
    model = DetalleVenta
    raw_id_fields = ("articulo",)
    fields = ['articulo','cantidad','desde', 'hasta', 'precio']
    
    extra = 1

class VentaAdmin(admin.ModelAdmin):
    fields = ['monto', 'fecha', 'medio_pago', 'cliente', 'num_tarjeta', 'administrador']
    inlines = [DetalleVentaInline]    
admin.site.register(Venta, VentaAdmin)


class RutinaClienteAdmin(admin.ModelAdmin):
    fields = ['cliente', 'rutina', 'actual']
admin.site.register(RutinaCliente, RutinaClienteAdmin)

#fsdfdsfdsfsfdsfds
""" class SerieInline(admin.TabularInline):
    model = Serie
    raw_id_fields = ("numero",)
    fields = ['numero', 'peso_levantado', 'repeticiones']
    extra = 1

class RegistroAdmin(admin.ModelAdmin):
    fields = ['cliente', 'rutina', 'ejercicio', 'completado']
    inlines = [SerieInline]
    admin.site.register(Registro, RegistroAdmin) """

