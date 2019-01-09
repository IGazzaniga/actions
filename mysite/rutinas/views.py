from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rutinas.models import Cliente, Profesor, RutinaCliente, Rutina, Venta, DetalleVenta, Dia
from django.shortcuts import get_object_or_404

# Create your views here.


@login_required
def index_view(request):
    usuario= None
    if request.user.is_authenticated:
        usuario = request.user
        if usuario.groups.filter(name='Clientes').exists():
        #Si pertenece al grupo Clientes, va a inicio-alumno
                cliente = Cliente.objects.get(user=usuario)
                rutinas = RutinaCliente.objects.filter(cliente=cliente, actual=True).first()
                rutina = rutinas.rutina.id
                return render(request, "rutinas/inicio-alumno.html",
        {'cliente': cliente, 'usuario': usuario, 'rutina': rutina})

        elif usuario.groups.filter(name='Profesores').exists():
        #Si pertenece al grupo Profesores, va a inicio-profe
                profesor = Profesor.objects.get(user=usuario)
                lista_clientes = Cliente.objects.filter(profesor=profesor)
        return render(request, "rutinas/inicio-profe.html",
         {'usuario': usuario, 'profesor': profesor, 'lista_clientes': lista_clientes})
    
@login_required
def rutina_view(request, id):
    usuario= None
    if request.user.is_authenticated:
        cliente = Cliente.objects.get(user=request.user)
        rutinas = Rutina.objects.get(id=id)
        dia1 = Dia.objects.filter(rutina=rutinas)[0]
        dia1 = dia1.ejercicios.all()
        dia2 = Dia.objects.filter(rutina=rutinas)[1]
        dia2 = dia2.ejercicios.all()
        dia3 = Dia.objects.filter(rutina=rutinas)[2]
        dia3 = dia3.ejercicios.all()
        return render(request, "rutinas/rutina.html", {'cliente': cliente, 'dia1': dia1, 'dia2': dia2, 'dia3': dia3, 'rutinas': rutinas})

@login_required
def detalle_pago_view(request,id):
    usuario= None
    if request.user.is_authenticated:
        cliente = Cliente.objects.get(user=request.user)
        pago = Venta.objects.get(id=id)
        detalle = DetalleVenta.objects.filter(pago=pago)
        return render(request, 'rutinas/detalle-pago.html', {'usuario': usuario, 'detalle': detalle})

@login_required
def info_ejercicio_view(request):
    return render(request, "rutinas/info-ejercicio.html")

@login_required
def inicio_profesor_view(request):
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


