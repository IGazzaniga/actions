from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rutinas.models import Cliente, Profesor

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

@login_required
def inicio_profesor_view(request):
    clientes = Cliente.objects.all().order_by('-nombre')
    return render(request, 'rutinas/inicio-profe.html', {'clientes': clientes})

@login_required
def calificar_view(request):
    profesores = Profesor.objects.all().order_by('-nombre')
    return render(request, 'rutinas/calificar.html', {'profesores': profesores})