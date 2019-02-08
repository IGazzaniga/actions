from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.decorators import login_required
from rutinas.models import Cliente, Servicio, FichaMedica, Profesor, RutinaCliente, Producto, Rutina, Venta, DetalleVenta, Dia, Articulo, Ejercicio
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
import datetime
from .forms import VentaForm, RutinaForm, DiaForm, RutinaClienteForm
from django.template import RequestContext
from dateutil.relativedelta import relativedelta

# Create your views here.


@login_required
def index_view(request):
    usuario= None
    if request.user.is_authenticated:
        usuario = request.user
        if usuario.groups.filter(name='Clientes').exists():
        #Si pertenece al grupo Clientes, va a inicio-alumno
                cliente = Cliente.objects.get(user=usuario)
                rutinas = RutinaCliente.objects.filter(cliente=cliente, actual=True)[0]
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
def info_ejercicio_view(request):
    return render(request, "rutinas/info-ejercicio.html")

@login_required
def calificar_view(request):
    profesores = Profesor.objects.all().order_by('-nombre')
    return render(request, 'rutinas/calificar.html', {'profesores': profesores})

@login_required
def nueva_rutina_view(request):
    if request.method == "POST":
        form = RutinaForm(request.POST)
        dia_form_1 = DiaForm(request.POST)
        dia_form_2 = DiaForm(request.POST)
        dia_form_3 = DiaForm(request.POST)
        if form.is_valid() and dia_form_1.is_valid() and dia_form_2.is_valid() and dia_form_3.is_valid():
            rutina = form.save(commit=False)
            dia1 = dia_form_1.save(commit=False)
            dia2 = dia_form_2.save(commit=False)
            dia3 = dia_form_3.save(commit=False)
            rutina.save()
            dia1.rutina = rutina
            dia2.rutina = rutina
            dia3.rutina = rutina
            ej = Ejercicio.objects.get(id=request.POST.get("ejercicios"))
            dia1.save()
            dia2.save()
            dia3.save()
            dia1.ejercicios.add(ej)
            dia2.ejercicios.add(ej)
            dia3.ejercicios.add(ej)
            dia1.save()
            dia2.save()
            dia3.save()
            return redirect(index_view)
    else:
        form = RutinaForm()
        dia_form_1 = DiaForm()
        dia_form_2 = DiaForm()
        dia_form_3 = DiaForm()        
    return render(request, 'rutinas/nueva-rutina.html', {'form': form, 'dia_form_1': dia_form_1, 'dia_form_2': dia_form_2, 'dia_form_3': dia_form_3})

@login_required
def perfil_alumno_view(request):
    usuario= None
    if request.user.is_authenticated:
        usuario = request.user
        cliente = Cliente.objects.get(user=usuario)
        ficha = FichaMedica.objects.get(cliente=cliente)
        return render(request, 'rutinas/perfil-alumno.html', {'usuario': usuario, 'ficha':ficha, 'cliente': cliente})

@login_required
def historial_rutinas_view(request,id):
    usuario= None
    if request.user.is_authenticated:
        cliente = Cliente.objects.get(id=id)
        rutinas = cliente.rutinas.all()
        return render(request, 'rutinas/historial-rutinas.html', {'usuario': usuario, 'cliente':cliente, 'rutinas': rutinas})

@login_required
def historial_rutinas_cliente_view(request):
    usuario= None
    if request.user.is_authenticated:
        rutinas = Cliente.objects.get(user=request.user).rutinas.all()
        return render(request, 'rutinas/historial-rutinas-cliente.html', {'usuario': usuario, 'rutinas': rutinas})

@login_required
def asignar_rutina_view(request, id):
    usuario= None
    cliente = Cliente.objects.get(id=id)
    if request.method == 'POST':
        form = RutinaClienteForm()
        rc = form.save(commit=False)
        rc.cliente = cliente
        rc.rutina = Rutina.objects.get(id = request.POST['rutina'])
        rc.actual = True
        rc.save()
        return redirect('rutinas')
    else:
        form = RutinaClienteForm()
    return render(request, 'rutinas/asignar-rutina.html', {'form': form, 'cliente': cliente,})

@login_required
def pagos_view(request):
    usuario= None
    if request.user.is_authenticated:
        cliente = Cliente.objects.get(user=request.user)
        pagos = Venta.objects.filter(cliente=cliente).order_by('-fecha')
        return render(request, 'rutinas/pagos.html', {'cliente': cliente, 'pagos': pagos})

@login_required
def registro_view(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            registro = form.save(commit=False)
            cliente = Cliente.objects.get(user=usuario)
            registro.cliente = cliente
            rutina = RutinaCliente.objects.filter(cliente=cliente, actual=True)
            registro.rutina = rutina
            registro.ejercicio = rutina
            rutina.save()
            return redirect('blog.views.rutina_detail', pk=rutina.pk)
    else:
        form = RegistroForm()          
    return render(request, 'rutinas/nueva-rutina.html', {'form': form})

def detalle_pago_view(request,id):
    usuario= None
    if request.user.is_authenticated:
        cliente = Cliente.objects.get(user=request.user)
        pago = Venta.objects.get(id=id)
        detalle = DetalleVenta.objects.filter(pago=pago)
        return render(request, 'rutinas/detalle-pago.html', {'usuario': usuario, 'detalle': detalle})

@login_required
def catalog_view(request):
    productos = Producto.objects.filter(stock__gt= 0)
    servicios = Servicio.objects.all()
    return render(request, 'rutinas/catalogo.html', {'productos': productos, 'servicios': servicios})

@login_required
def detalle_producto_view(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'rutinas/detalle-producto.html', {'producto': producto})

@login_required
def detalle_servicio_view(request, id):
    servicio = get_object_or_404(Servicio, id=id)
    desde = datetime.date.today()
    hasta = desde + relativedelta(months=1)
    return render(request, 'rutinas/detalle-servicio.html', {'desde':desde, 'hasta':hasta, 'servicio': servicio})

@login_required
def comprar_view(request, id):
    user = request.user
    cliente = Cliente.objects.get(user=request.user)
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
                venta = form.save(commit=False)
                # commit=False tells Django that "Don't send this to database yet.
                # I have more things I want to do with it."
                venta.cliente = cliente # Set the user object here
                venta.monto = producto.precio
                venta.fecha = datetime.datetime.now()
                detalle_venta = DetalleVenta()
                detalle_venta.cantidad = 1
                detalle_venta.precio = producto.precio
                detalle_venta.articulo = producto
                venta.save() # Now you can send it to DB  
                detalle_venta.pago = venta              
                detalle_venta.save() 
                venta.save()
                producto.stock = producto.stock - 1
                producto.save()

                return redirect('pago_procesado')
    else:
        form = VentaForm()
    return render(request, 'rutinas/comprar.html', {'form': form, 'cliente': cliente,'producto': producto})

@login_required
def pagar_view(request, id):
    user = request.user
    cliente = Cliente.objects.get(user=request.user)
    servicio = get_object_or_404(Servicio, id=id)
    desde = datetime.date.today()
    hasta = desde + relativedelta(months=1)
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
                venta = form.save(commit=False)
                # commit=False tells Django that "Don't send this to database yet.
                # I have more things I want to do with it."
                venta.cliente = cliente # Set the user object here
                venta.monto = servicio.precio
                venta.fecha = datetime.datetime.now()
                detalle_venta = DetalleVenta()
                detalle_venta.cantidad = 1
                detalle_venta.precio = servicio.precio
                detalle_venta.articulo = servicio
                detalle_venta.desde = desde
                detalle_venta.hasta = hasta
                venta.save() # Now you can send it to DB  
                detalle_venta.pago = venta              
                detalle_venta.save() 
                venta.save()

                return redirect('pago_procesado')
    else:
        form = VentaForm()
    return render(request, 'rutinas/pagar.html', {'desde':desde, 'hasta':hasta, 'form': form, 'cliente': cliente,'servicio': servicio})

@login_required
def pago_procesado_view(request):
    return render(request, 'rutinas/pago-procesado.html')
        
@login_required
def perfil_profe_view(request,id):
    profesor = get_object_or_404(Profesor, id=id)
    return render(request, 'rutinas/perfil-profe.html', {'profesor': profesor})

@login_required
def detalle_ejercicio_view(request, id):
        ejercicio = get_object_or_404(Ejercicio, id=id)
        return render(request, 'rutinas/detalle-ejercicio.html', {'ejercicio': ejercicio})