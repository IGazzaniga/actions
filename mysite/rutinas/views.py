from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rutinas.models import Cliente, Profesor, RutinaCliente, Rutina, Venta

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

@login_required
def nueva_rutina_view(request):
    if request.method == "POST":
        form = RutinaForm(request.POST)
        if form.is_valid():
            rutina = form.save(commit=False)
            rutina.author = request.user
            rutina.published_date = timezone.now()
            rutina.save()
            return redirect('blog.views.rutina_detail', pk=rutina.pk)
    else:
        form = RutinaForm()          
    return render(request, 'rutinas/nueva-rutina.html', {'form': form})

@login_required
def perfil_alumno_view(request):
    usuario= None
    if request.user.is_authenticated:
        usuario = request.user
        cliente = Cliente.objects.get(user=usuario)
        return render(request, 'rutinas/perfil-alumno.html', {'usuario': usuario, 'cliente': cliente})

@login_required
def historial_rutinas_view(request):
    usuario= None
    if request.user.is_authenticated:
        rutinas = Cliente.objects.get(user=request.user).rutinas.all()
        return render(request, 'rutinas/historial-rutinas.html', {'usuario': usuario, 'rutinas': rutinas})

@login_required
def pagos_view(request):
    usuario= None
    if request.user.is_authenticated:
        cliente = Cliente.objects.get(user=request.user)
        pagos = Venta.objects.filter(cliente=cliente)
        return render(request, 'rutinas/pagos.html', {'usuario': usuario, 'pagos': pagos})