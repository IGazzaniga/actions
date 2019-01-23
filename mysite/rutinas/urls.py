"""Rutinas urls."""

from django.conf.urls import include, url
from django.contrib import admin
from . import views
from rutinas.views import detalle_producto_view,catalog_view, detalle_pago_view, index_view, pagos_view, historial_rutinas_view, info_ejercicio_view, perfil_alumno_view, calificar_view, inicio_profesor_view, rutina_view, nueva_rutina_view #Importamos las vistas



urlpatterns = [
    url(r'^$', index_view, name="rutinas"),
    url(r'^rutinaAlumno/(?P<id>[\w-]+)$', rutina_view, name="rutinaAlumno"),
    url(r'^infoEjercicio', info_ejercicio_view, name="infoEjercicio"),
    url(r'^inicioProfe', inicio_profesor_view, name="inicioProfe"),
    url(r'^calificar', calificar_view, name="calificar"),
    url(r'^perfil_alumno', perfil_alumno_view, name="perfil_alumno"),
    url(r'^nueva_rutina', nueva_rutina_view, name="nueva_rutina"),
    url(r'^historialRutinas', historial_rutinas_view, name="historial_rutinas"),
    url(r'^pagos', pagos_view, name="pagos"),
    url(r'^detalle_pago/(?P<id>[\w-]+)$', detalle_pago_view, name="detalle_pago"),
    url(r'^catalogo', catalog_view, name='catalogo'),
    url(r'^detalle_producto/(?P<id>[\w-]+)$', detalle_producto_view, name="detalle_producto")
    
]