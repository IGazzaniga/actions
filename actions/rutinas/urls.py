"""Rutinas urls."""

from django.urls import include, path
from django.conf.urls import url
from django.contrib import admin
from . import views
from rutinas.views import *  # Importamos las vistas
from rest_framework import routers


urlpatterns = [
    url(r"^$", index_view, name="rutinas"),
    url(r"^rutinaAlumno/(?P<id>[\w-]+)$", rutina_view, name="rutinaAlumno"),
    url(r"^calificar", calificar_view, name="calificar"),
    url(r"^perfil_alumno", perfil_alumno_view, name="perfil_alumno"),
    url(r"^nueva_rutina", nueva_rutina_view, name="nueva_rutina"),
    url(r"^historialRutinas/(?P<id>[\w-]+)$", historial_rutinas_view, name="historial_rutinas"),
    url(r"^historialRutinasAlumno", historial_rutinas_cliente_view, name="historial_rutinas_cliente"),
    url(r"^pagos", pagos_view, name="pagos"),
    url(r"^detalle_pago/(?P<id>[\w-]+)$", detalle_pago_view, name="detalle_pago"),
    url(r"^catalogo", catalog_view, name="catalogo"),
    url(r"^detalle_producto/(?P<id>[\w-]+)$", detalle_producto_view, name="detalle_producto"),
    url(r"^detalle_servicio/(?P<id>[\w-]+)$", detalle_servicio_view, name="detalle_servicio"),
    url(r"^comprar/(?P<id>[\w-]+)$", comprar_view, name="comprar"),
    url(r"^pagar/(?P<id>[\w-]+)$", pagar_view, name="pagar"),
    url(r"^perfil/(?P<id>[\w-]+)$", perfil_profe_view, name="perfil_profe"),
    url(r"^ver_perfil_alumno/(?P<id>[\w-]+)$", ver_perfil_alumno_view, name="ver_perfil_alumno"),
    url(r"^editarPerfilProfe", editar_perfil_profe_view, name="editar_perfil_profe"),
    url(r"^pago_procesado", pago_procesado_view, name="pago_procesado"),
    url(
        r"^registro_ejercicio/(?P<r>[\w-]+)-(?P<e>[\w-]+)-(?P<d>[\w-]+)-(?P<s>[\w-]+)$",
        registro_ejercicio_view,
        name="registro_ejercicio",
    ),
    url(r"^asignar_rutina/(?P<id>[\w-]+)$", asignar_rutina_view, name="asignar_rutina"),
    url(r"^detalle_rutina/(?P<id>[\w-]+)$", rutina_detalle_view, name="detalle_rutina"),
]
