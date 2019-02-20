from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.decorators import login_required
from rutinas.models import RutinaEjercicio,Registro, Cliente, Semana, Servicio, FichaMedica, Profesor, RutinaCliente, Producto, Rutina, Venta, DetalleVenta, Dia, Articulo, Ejercicio, Serie
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
import datetime
from .forms import VentaForm, ProfesorForm, RutinaForm, DiaForm, RutinaClienteForm, SerieForm, RegistroForm, ClienteForm, FichaForm
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
                rutinas = RutinaCliente.objects.get(cliente=cliente, actual=True)
                rutinacliente = rutinas.id
                return render(request, "rutinas/inicio-alumno.html",
        {'cliente': cliente, 'usuario': usuario, 'rutinacliente': rutinacliente})

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
        rc = RutinaCliente.objects.get(id=id)
        semana = Semana.objects.filter(rutina_cliente=rc)
        rutina_ejercicio = RutinaEjercicio.objects.filter(rutina= rc.rutina)
        return render(request, "rutinas/rutina.html", {'s': semana, 'cliente': cliente, 'rc': rc, 'rutina_ejercicio': rutina_ejercicio})

@login_required
def info_ejercicio_view(request):
    return render(request, "rutinas/info-ejercicio.html")

@login_required
def calificar_view(request): 
    usuario= None
    if request.user.is_authenticated:
        cliente = Cliente.objects.get(user=request.user)
        profesores = Profesor.objects.all().order_by('-nombre')
        return render(request, 'rutinas/calificar.html', {'cliente':cliente, 'profesores': profesores})

@login_required
def ver_perfil_alumno_view(request, id): 
    usuario= None
    if request.user.is_authenticated:
        profesor = Profesor.objects.get(user=request.user)
        cliente = Cliente.objects.get(id=id)
        return render(request, 'rutinas/ver-perfil-alumno.html', {'profesor':profesor, 'cliente': cliente})

@login_required
def rutina_detalle_view(request, id):
    usuario = None
    if request.user.is_authenticated:
        profesor = Profesor.objects.get(user=request.user)
        rutina = Rutina.objects.get(id=id)
        dias = Dia.objects.filter(rutina=rutina)
        ejercicios = RutinaEjercicio.objects.filter(rutina=rutina)
        return render(request, 'rutinas/detalle-rutina.html', {'profesor':profesor, 'rutina':rutina, 'dias': dias, 'ejercicios':ejercicios})


@login_required
def nueva_rutina_view(request):
    profesor = Profesor.objects.get(user=request.user)
    if request.method == "POST":
        form = RutinaForm(request.POST)
        dia_form_1 = DiaForm(request.POST, prefix='dia1')
        dia_form_2 = DiaForm(request.POST, prefix='dia2')
        dia_form_3 = DiaForm(request.POST, prefix='dia3')
        if form.is_valid() and dia_form_1.is_valid() and dia_form_2.is_valid() and dia_form_3.is_valid():
            rutina = form.save(commit=False)
            dia1 = dia_form_1.save(commit=False)
            dia2 = dia_form_2.save(commit=False)
            dia3 = dia_form_3.save(commit=False)
            rutina.save()
            dia1.rutina = rutina
            dia2.rutina = rutina
            dia3.rutina = rutina
            dia1.save() #Guardo todos los días así su id no es vacío
            dia2.save()
            dia3.save()
            #A continuación, en ej1 guardo la lista de los ejercicios que seleccioné para el día 1
            ej1 = Ejercicio.objects.filter(id__in = request.POST.getlist('dia1-ejercicios'))
            for e in ej1:
                RutinaEjercicio.objects.create(ejercicio=e,rutina=rutina,dia=dia1)
            ej2 = Ejercicio.objects.filter(id__in = request.POST.getlist('dia2-ejercicios'))
            for e in ej2:
                RutinaEjercicio.objects.create(ejercicio=e,rutina=rutina,dia=dia2)
            ej3 = Ejercicio.objects.filter(id__in = request.POST.getlist('dia3-ejercicios'))
            for e in ej3:
                RutinaEjercicio.objects.create(ejercicio=e,rutina=rutina,dia=dia3)
            #Le asigno esa lista a los ejercicios del día 1
            dia1.ejercicios.set(ej1)
            dia2.ejercicios.set(ej2)
            dia3.ejercicios.set(ej3)
            dia1.save()
            dia2.save()
            dia3.save()
            return redirect(index_view)
    else:
        form = RutinaForm()
        dia_form_1 = DiaForm(prefix='dia1')
        dia_form_2 = DiaForm(prefix='dia2')
        dia_form_3 = DiaForm(prefix='dia3')        
    return render(request, 'rutinas/nueva-rutina.html', {'profesor':profesor, 'form': form, 'dia_form_1': dia_form_1, 'dia_form_2': dia_form_2, 'dia_form_3': dia_form_3})

@login_required
def editar_rutina_view(request, id):
    profesor = Profesor.objects.get(user=request.user)
    rutina = Rutina.objects.get(id=id)
    dia1 = Dia.objects.filter(rutina=rutina)[0]
    dia2 = Dia.objects.filter(rutina=rutina)[1]
    dia3 = Dia.objects.filter(rutina=rutina)[2]
    if request.method == "POST":
        form = RutinaForm(request.POST, instance=rutina)
        dia_form_1 = DiaForm(request.POST, instance= dia1, prefix='dia1')
        dia_form_2 = DiaForm(request.POST, instance= dia2, prefix='dia2')
        dia_form_3 = DiaForm(request.POST, instance= dia3, prefix='dia3')
        if form.is_valid() and dia_form_1.is_valid() and dia_form_2.is_valid() and dia_form_3.is_valid():
            rutina = form.save(commit=False)
            dia1 = dia_form_1.save(commit=False)
            dia2 = dia_form_2.save(commit=False)
            dia3 = dia_form_3.save(commit=False)
            rutina.save()
            dia1.rutina = rutina
            dia2.rutina = rutina
            dia3.rutina = rutina
            dia1.save() #Guardo todos los días así su id no es vacío
            dia2.save()
            dia3.save()
            #A continuación, en ej1 guardo la lista de los ejercicios que seleccioné para el día 1
            ej1 = Ejercicio.objects.filter(id__in = request.POST.getlist('dia1-ejercicios'))
            for e in ej1:
                RutinaEjercicio.objects.create(ejercicio=e,rutina=rutina,dia=dia1)
            ej2 = Ejercicio.objects.filter(id__in = request.POST.getlist('dia2-ejercicios'))
            for e in ej2:
                RutinaEjercicio.objects.create(ejercicio=e,rutina=rutina,dia=dia2)
            ej3 = Ejercicio.objects.filter(id__in = request.POST.getlist('dia3-ejercicios'))
            for e in ej3:
                RutinaEjercicio.objects.create(ejercicio=e,rutina=rutina,dia=dia3)
            #Le asigno esa lista a los ejercicios del día 1
            dia1.ejercicios.set(ej1)
            dia2.ejercicios.set(ej2)
            dia3.ejercicios.set(ej3)
            dia1.save()
            dia2.save()
            dia3.save()
            return redirect(index_view)
    else:
        form = RutinaForm()
        dia_form_1 = DiaForm(prefix='dia1')
        dia_form_2 = DiaForm(prefix='dia2')
        dia_form_3 = DiaForm(prefix='dia3')        
    return render(request, 'rutinas/editar-rutina.html', {'rutina':rutina, 'dia1':dia1, 'dia2':dia2, 'dia3':dia3, 'profesor':profesor, 'form': form, 'dia_form_1': dia_form_1, 'dia_form_2': dia_form_2, 'dia_form_3': dia_form_3})


@login_required
def historial_rutinas_view(request,id):
    usuario= None
    if request.user.is_authenticated:
        cliente = Cliente.objects.get(id=id)
        profesor = Profesor.objects.get(user=request.user)
        rutinas = cliente.rutinas.all()
        return render(request, 'rutinas/historial-rutinas.html', {'profesor':profesor, 'usuario': usuario, 'cliente':cliente, 'rutinas': rutinas})

@login_required
def historial_rutinas_cliente_view(request):
    usuario= None
    if request.user.is_authenticated:
        cliente = Cliente.objects.get(user=request.user)
        rutinas = RutinaCliente.objects.filter(cliente=cliente)
        return render(request, 'rutinas/historial-rutinas-cliente.html', {'cliente':cliente, 'usuario': usuario, 'rutinas': rutinas})

@login_required
def asignar_rutina_view(request, id):
    usuario= None
    cliente = Cliente.objects.get(id=id)
    profesor = Profesor.objects.get(user=request.user)
    if request.method == 'POST':
        form = RutinaClienteForm()
        rc = form.save(commit=False)
        rc.cliente = cliente
        rc.rutina = Rutina.objects.get(id = request.POST['rutina'])
        rc.actual = True
        rc.save()
        d = Dia.objects.filter(rutina = rc.rutina.id)
        for i in range(1, 5):
               s = Semana.objects.create(numero=i,rutina_cliente=rc)
               s.dias.set(d)
               s.save()
        return redirect('rutinas')
    else:
        form = RutinaClienteForm()
    return render(request, 'rutinas/asignar-rutina.html', {'profesor':profesor, 'form': form, 'cliente': cliente,})

@login_required
def pagos_view(request):
    usuario= None
    if request.user.is_authenticated:
        cliente = Cliente.objects.get(user=request.user)
        pagos = Venta.objects.filter(cliente=cliente).order_by('-fecha')
        return render(request, 'rutinas/pagos.html', {'cliente': cliente, 'pagos': pagos})

def detalle_pago_view(request,id):
    usuario= None
    if request.user.is_authenticated:
        cliente = Cliente.objects.get(user=request.user)
        pago = Venta.objects.get(id=id)
        detalle = DetalleVenta.objects.filter(pago=pago)
        return render(request, 'rutinas/detalle-pago.html', {'usuario': usuario, 'detalle': detalle})

@login_required
def catalog_view(request):
    usuario= None
    if request.user.is_authenticated:
        cliente = Cliente.objects.get(user=request.user)
        productos = Producto.objects.filter(stock__gt= 0)
        servicios = Servicio.objects.all()
        return render(request, 'rutinas/catalogo.html', {'cliente':cliente, 'productos': productos, 'servicios': servicios})

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
def perfil_alumno_view(request):
    usuario= None
    if request.user.is_authenticated:
        usuario = request.user
        cliente = Cliente.objects.get(user=usuario)
        ficha_medica = FichaMedica.objects.get(cliente=cliente)
        if request.method == 'POST':
            form = ClienteForm(request.POST, request.FILES)
            ficha = FichaForm(request.POST, instance=ficha_medica)
            foto = request.FILES['foto']
            if form.is_valid() and ficha.is_valid():
                fm = ficha.save(commit=False)
                fm.altura = request.POST.get('altura')
                fm.peso = request.POST.get('peso')
                fm.sexo = request.POST.get('sexo')
                fm.mutual = request.POST.get('mutual')
                fm.observaciones = request.POST.get('observaciones')
                fm.telefono_emergencia = request.POST.get('telefono_emergencia')
                fm.cliente = cliente
                fm.save()
                perfil = form.save(commit=False)
                perfil.user = request.user
                perfil.nombre = request.POST.get('nombre')
                perfil.apellido = request.POST.get('apellido')
                perfil.dni = request.POST.get('dni')
                perfil.telefono = request.POST.get('telefono')
                perfil.domicilio = request.POST.get('domicilio')
                perfil.profesor = cliente.profesor
                perfil.id = cliente.id
                perfil.save()
                return redirect(index_view)
            else:
                print(form.errors)
                print(form.non_field_errors)
                print(ficha.errors)
                print(ficha.non_field_errors)
        else:
            form = ClienteForm()
            ficha = FichaForm()
        return render(request, 'rutinas/perfil-alumno.html', {'ficha':ficha, 'form': form, 'usuario': usuario, 'cliente': cliente})

@login_required
def editar_perfil_profe_view(request):
    usuario= None
    if request.user.is_authenticated:
        usuario = request.user
        profesor = Profesor.objects.get(user=usuario)
        if request.method == 'POST':
            form = ProfesorForm(request.POST, request.FILES)
            foto = request.FILES['foto']
            if form.is_valid():
                perfil = form.save(commit=False)
                perfil.user = request.user
                perfil.nombre = request.POST.get('nombre')
                perfil.apellido = request.POST.get('apellido')
                perfil.telefono = request.POST.get('telefono')
                perfil.domicilio = request.POST.get('domicilio')
                perfil.id = profesor.id
                perfil.save()
                return redirect(index_view)
            else:
                print(form.errors)
                print(form.non_field_errors)
        else:
            form = ProfesorForm()
        return render(request, 'rutinas/editar-perfil-profe.html', {'form': form, 'usuario': usuario, 'profesor': profesor})

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
def registro_ejercicio_view(request, r, e, d, s):
        cliente = Cliente.objects.get(user=request.user)
        re = RutinaEjercicio.objects.get(ejercicio=e, rutina=r, dia=d)
        sem = Semana.objects.get(id=s)
        try:
                reg = Registro.objects.get(rutina_ejercicio__ejercicio=e, rutina_ejercicio__rutina=r, rutina_ejercicio__dia=d, semana=s)
        except Registro.DoesNotExist:
                reg = Registro.objects.create(rutina_ejercicio=re, semana=sem)
                form = SerieForm()
                return render(request, 'rutinas/registro-ejercicio.html', {'r':r, 'e':e, 'd':d, 's':s, 'form': form, 'sem': sem, 'reg': reg, 'cliente': cliente})
        else:
                if request.method == 'POST':
                        if request.POST['completado'] == "True":
                                rf = RegistroForm(instance=reg)
                                rnew = rf.save(commit=False)
                                rnew.completado = True
                                rnew.save()
                                rc = RutinaCliente.objects.get(cliente=cliente, actual=True)
                                return redirect(rutina_view, id=rc.id)                               
                        try:
                                ser = Serie.objects.get(numero=request.POST['id_numero'], registro=reg)
                        except Serie.DoesNotExist:
                                form = SerieForm()
                                serie = form.save(commit=False)
                                serie.numero = request.POST['id_numero']
                                serie.peso_levantado = request.POST['id_peso_levantado']
                                serie.repeticiones = request.POST['id_repeticiones']
                                serie.registro = reg
                                serie.save()
                                return redirect(registro_ejercicio_view, r=r, e=e, d=d, s=s)
                        else:
                                f = SerieForm(instance=ser)
                                snew = f.save(commit=False)
                                snew.peso_levantado = request.POST['id_peso_levantado']
                                snew.repeticiones = request.POST['id_repeticiones']
                                snew.save()
                                return redirect(registro_ejercicio_view, r=r, e=e, d=d, s=s)
                form = SerieForm()
                return render(request, 'rutinas/registro-ejercicio.html', {'r':r, 'e':e, 'd':d, 's':s, 'form': form, 'sem':sem, 'reg': reg, 'cliente': cliente})
