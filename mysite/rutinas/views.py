from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rutinas.models import Cliente

# Create your views here.


@login_required
def index_view(request):
    return render(request, "rutinas/inicio-alumno.html")
    
@login_required
def rutina_view(request):
    return render(request, "rutinas/rutina.html")

@login_required
def info_ejercicio_view(request):
    return render(request, "rutinas/info-ejercicio.html")

