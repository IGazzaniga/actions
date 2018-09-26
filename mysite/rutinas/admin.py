from django.contrib import admin
from .models import (Proveedor, Sucursal, Producto, 
Administrador, Profesor, Rutina, Ejercicio, Cliente, Pago, FichaMedica)


class AdministradorAdmin(admin.ModelAdmin):
    fields = ['user','nombre', 'apellido', 'sucursal']
admin.site.register(Administrador, AdministradorAdmin)

class SucursalAdmin(admin.ModelAdmin):
    fields = ['nombre', 'domicilio', 'telefono']
admin.site.register(Sucursal, SucursalAdmin)

class ProveedorAdmin(admin.ModelAdmin):
    fields = ['nombre', 'apellido', 'mail','telefono']

admin.site.register(Proveedor, ProveedorAdmin)

class ProductoAdmin(admin.ModelAdmin):
    fields = ['nombre','tipo_producto', 'proveedor', 'sucursal']
admin.site.register(Producto, ProductoAdmin)

class ProfesorAdmin(admin.ModelAdmin):
    fields = ['user', 'nombre', 'apellido', 'num_matricula', 'mail', 'telefono', 'domicilio']

admin.site.register(Profesor, ProfesorAdmin)

class EjercicioAdmin(admin.ModelAdmin):
    fields = ['nombre', 'gif','tren']
admin.site.register(Ejercicio, EjercicioAdmin)

class RutinaAdmin(admin.ModelAdmin):
    fields = ['numero','sesiones', 'ejercicios'] 
    

admin.site.register(Rutina, RutinaAdmin)

class FichaMedicaInline(admin.TabularInline):
    model = FichaMedica
    fields = ['fecha_nacimiento', 'altura', 'peso', 'sexo', 'mutual', 'observaciones', 'telefono_emergencia']

class ClienteAdmin(admin.ModelAdmin):
    fields = ['user', 'nombre', 'apellido', 'dni', 'mail', 'telefono', 'domicilio', 'profesor', 'rutinas']
    inlines = [FichaMedicaInline]

admin.site.register(Cliente, ClienteAdmin)


class PagoAdmin(admin.ModelAdmin):
    fields = ['monto', 'fecha', 'medio_pago', 'cliente']

admin.site.register(Pago, PagoAdmin)

