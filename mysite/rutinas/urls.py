"""Rutinas urls."""

from django.conf.urls import include, url
from django.contrib import admin
from . import views
from rutinas.views import pago_procesado_view, detalle_servicio_view, comprar_view, perfil_profe_view, detalle_producto_view,catalog_view, pagar_view, detalle_pago_view, index_view, pagos_view, historial_rutinas_view, info_ejercicio_view, perfil_alumno_view, calificar_view, rutina_view, nueva_rutina_view, detalle_ejercicio_view #Importamos las vistas



urlpatterns = [
    url(r'^$', index_view, name="rutinas"),
    url(r'^rutinaAlumno/(?P<id>[\w-]+)$', rutina_view, name="rutinaAlumno"),
    url(r'^infoEjercicio', info_ejercicio_view, name="infoEjercicio"),
    url(r'^calificar', calificar_view, name="calificar"),
    url(r'^perfil_alumno', perfil_alumno_view, name="perfil_alumno"),
    url(r'^nueva_rutina', nueva_rutina_view, name="nueva_rutina"),
    url(r'^historialRutinas', historial_rutinas_view, name="historial_rutinas"),
    url(r'^pagos', pagos_view, name="pagos"),
    url(r'^detalle_pago/(?P<id>[\w-]+)$', detalle_pago_view, name="detalle_pago"),
    url(r'^catalogo', catalog_view, name='catalogo'),
    url(r'^detalle_producto/(?P<id>[\w-]+)$', detalle_producto_view, name="detalle_producto"),
    url(r'^detalle_servicio/(?P<id>[\w-]+)$', detalle_servicio_view, name="detalle_servicio"),
    url(r'^comprar/(?P<id>[\w-]+)$', comprar_view, name="comprar"),
    url(r'^pagar/(?P<id>[\w-]+)$', pagar_view, name="pagar"),
    url(r'^perfil/(?P<id>[\w-]+)$', perfil_profe_view, name="perfil_profe"),
    url(r'^pago_procesado', pago_procesado_view, name="pago_procesado"),
    url(r'^detalle_ejercicio/(?P<id>[\w-]+)$', detalle_ejercicio_view, name="detalle_ejercicio"),
        
]