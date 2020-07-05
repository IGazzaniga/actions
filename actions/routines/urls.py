"""Rutinas urls."""

from django.urls import path
from routines.views import index_view

urlpatterns = [
    path("", index_view),
]
