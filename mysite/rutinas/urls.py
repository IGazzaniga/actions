"""Rutinas urls."""

from django.conf.urls import include, url
from django.contrib import admin
from . import views
from rutinas.views import index_view, rutina_view #Importamos las vistas



urlpatterns = [
    url(r'^$', index_view, name="rutinas"),
    url(r'^rutinaAlumno', rutina_view, name="rutinaAlumno"),
]