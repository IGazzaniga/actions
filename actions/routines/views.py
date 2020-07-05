# import datetime
#
# from dateutil.relativedelta import relativedelta
# from django.contrib.auth.decorators import login_required
# from django.http import Http404
# from django.shortcuts import get_object_or_404, redirect, render
# from django.template import RequestContext
# from django.urls import reverse
#
# from .models import (
#    Day,
#    Exercise,
#    Register,
#    Routine,
#    RoutineClient,
#    RoutineExercise,
#    Serie,
#    Week,
# )

# Create your views here.


""" @login_required
def index_view(request):
    user = None
    if request.user.is_authenticated:
        user = request.user
        if user.groups.filter(name="Clients").exists():
            # Si pertenece al grupo Clients, va a inicio-alumno
            client = Client.objects.get(user=user)
            try:
                routine = RoutineClient.objects.get(client=client, is_current=True)
                routine_client = routines.id
                return render(
                    request,
                    "routines/inicio-alumno.html",
                    {"client": client, "user": user, "routine_client": routine_client,},
                )
            except RoutineClient.DoesNotExist:
                return render(
                    request,
                    "routines/inicio-alumno.html",
                    {"client": client, "user": user},
                )
        elif user.groups.filter(name="Profesores").exists():
            # Si pertenece al grupo Profesores, va a inicio-profe
            # profesor = Profesor.objects.get(user=user)
            lista_clients = Client.objects.filter(profesor=profesor)
        return render(
            request,
            "routines/inicio-profe.html",
            {"user": user, "profesor": profesor, "lista_clients": lista_clients,},
        )


@login_required
def rutina_view(request, id):
    user = None
    if request.user.is_authenticated:
        user = request.user
        if user.groups.filter(name="Clients").exists():
            client = Client.objects.get(user=request.user)
            rc = RoutineClient.objects.get(id=id)
            semana = Semana.objects.filter(rutina_client=rc)
            rutina_ejercicio = RoutineEjercicio.objects.filter(rutina=rc.rutina)
            return render(
                request,
                "routines/rutina.html",
                {
                    "s": semana,
                    "client": client,
                    "rc": rc,
                    "rutina_ejercicio": rutina_ejercicio,
                },
            )
        else:
            raise Http404("No tiene permiso para acceder aquí")


@login_required
def calificar_view(request):
    user = None
    if request.user.is_authenticated:
        user = request.user
        if user.groups.filter(name="Clients").exists():
            client = Client.objects.get(user=user)
            profesores = Profesor.objects.all().order_by("-nombre")
            return render(
                request,
                "routines/calificar.html",
                {"client": client, "profesores": profesores},
            )
        else:
            raise Http404("No tiene permiso para acceder aquí")


@login_required
def ver_perfil_alumno_view(request, id):
    user = None
    if request.user.is_authenticated:
        user = request.user
        if user.groups.filter(name="Profesores").exists():
            profesor = Profesor.objects.get(user=user)
            client = Client.objects.get(id=id)
            return render(
                request,
                "routines/ver-perfil-alumno.html",
                {"profesor": profesor, "client": client},
            )
        else:
            raise Http404("No tiene permiso para acceder aquí")


@login_required
def rutina_detalle_view(request, id):
    user = None
    if request.user.is_authenticated:
        user = request.user
        if user.groups.filter(name="Profesores").exists():
            profesor = Profesor.objects.get(user=user)
            rutina = Routine.objects.get(id=id)
            dias = Dia.objects.filter(rutina=rutina)
            ejercicios = RoutineEjercicio.objects.filter(rutina=rutina)
            return render(
                request,
                "routines/detalle-rutina.html",
                {
                    "profesor": profesor,
                    "rutina": rutina,
                    "dias": dias,
                    "ejercicios": ejercicios,
                },
            )
        else:
            raise Http404("No tiene permiso para acceder aquí")


@login_required
def nueva_rutina_view(request):
    user = None
    if request.user.is_authenticated:
        user = request.user
        profesor = Profesor.objects.get(user=user)
        if user.groups.filter(name="Profesores").exists():
            if request.method == "POST":
                form = RoutineForm(request.POST)
                dia_form_1 = DiaForm(request.POST, prefix="dia1")
                dia_form_2 = DiaForm(request.POST, prefix="dia2")
                dia_form_3 = DiaForm(request.POST, prefix="dia3")
                if (
                    form.is_valid()
                    and dia_form_1.is_valid()
                    and dia_form_2.is_valid()
                    and dia_form_3.is_valid()
                ):
                    rutina = form.save(commit=False)
                    dia1 = dia_form_1.save(commit=False)
                    dia2 = dia_form_2.save(commit=False)
                    dia3 = dia_form_3.save(commit=False)
                    rutina.save()
                    dia1.rutina = rutina
                    dia2.rutina = rutina
                    dia3.rutina = rutina
                    dia1.save()  # Guardo todos los días así su id no es vacío
                    dia2.save()
                    dia3.save()
                    # A continuación, en ej1 guardo la lista de los ejercicios que seleccioné para el día 1
                    ej1 = Ejercicio.objects.filter(
                        id__in=request.POST.getlist("dia1-ejercicios")
                    )
                    for e in ej1:
                        RoutineEjercicio.objects.create(
                            ejercicio=e, rutina=rutina, dia=dia1
                        )
                    ej2 = Ejercicio.objects.filter(
                        id__in=request.POST.getlist("dia2-ejercicios")
                    )
                    for e in ej2:
                        RoutineEjercicio.objects.create(
                            ejercicio=e, rutina=rutina, dia=dia2
                        )
                    ej3 = Ejercicio.objects.filter(
                        id__in=request.POST.getlist("dia3-ejercicios")
                    )
                    for e in ej3:
                        RoutineEjercicio.objects.create(
                            ejercicio=e, rutina=rutina, dia=dia3
                        )
                    # Le asigno esa lista a los ejercicios del día 1
                    dia1.ejercicios.set(ej1)
                    dia2.ejercicios.set(ej2)
                    dia3.ejercicios.set(ej3)
                    dia1.save()
                    dia2.save()
                    dia3.save()
                    return redirect(index_view)
            else:
                form = RoutineForm()
                dia_form_1 = DiaForm(prefix="dia1")
                dia_form_2 = DiaForm(prefix="dia2")
                dia_form_3 = DiaForm(prefix="dia3")
            return render(
                request,
                "routines/nueva-rutina.html",
                {
                    "profesor": profesor,
                    "form": form,
                    "dia_form_1": dia_form_1,
                    "dia_form_2": dia_form_2,
                    "dia_form_3": dia_form_3,
                },
            )
        else:
            raise Http404("No tiene permiso para acceder aquí")


@login_required
def historial_rutinas_view(request, id):
    user = None
    if request.user.is_authenticated:
        user = request.user
        if user.groups.filter(name="Profesores").exists():
            client = Client.objects.get(id=id)
            profesor = Profesor.objects.get(user=user)
            try:
                routines = RoutineClient.objects.filter(client=client)
                actual = RoutineClient.objects.get(actual=True, client=client)
                return render(
                    request,
                    "routines/historial-routines.html",
                    {
                        "actual": actual,
                        "profesor": profesor,
                        "user": user,
                        "client": client,
                        "routines": routines,
                    },
                )
            except RoutineClient.DoesNotExist:
                no_hay = True
                return render(
                    request,
                    "routines/historial-routines.html",
                    {
                        "no_hay": no_hay,
                        "profesor": profesor,
                        "user": user,
                        "client": client,
                    },
                )
            raise Http404("No tiene permiso para acceder aquí")


@login_required
def historial_rutinas_client_view(request):
    user = None
    if request.user.is_authenticated:
        user = request.user
        if user.groups.filter(name="Clients").exists():
            client = Client.objects.get(user=user)
            routines = RoutineClient.objects.filter(client=client)
            return render(
                request,
                "routines/historial-routines-client.html",
                {"client": client, "user": user, "routines": routines},
            )
        else:
            raise Http404("No tiene permiso para acceder aquí")


@login_required
def asignar_rutina_view(request, id):
    user = None
    if request.user.is_authenticated:
        user = request.user
        if user.groups.filter(name="Profesores").exists():
            user = request.user
            client = Client.objects.get(id=id)
            profesor = Profesor.objects.get(user=user)
            if request.method == "POST":
                form = RoutineClientForm()
                rc = form.save(commit=False)
                rc.client = client
                rc.rutina = Routine.objects.get(id=request.POST["rutina"])
                rc.actual = True
                rc.save()
                d = Dia.objects.filter(rutina=rc.rutina.id)
                for i in range(1, 5):
                    s = Semana.objects.create(numero=i, rutina_client=rc)
                    s.dias.set(d)
                    s.save()
                return redirect("routines")
            else:
                form = RoutineClientForm()
            return render(
                request,
                "routines/asignar-rutina.html",
                {"profesor": profesor, "form": form, "client": client,},
            )
    else:
        raise Http404("No tiene permiso para acceder aquí")


@login_required
def pagos_view(request):
    user = None
    if request.user.is_authenticated:
        user = request.user
        if user.groups.filter(name="Clients").exists():
            client = Client.objects.get(user=request.user)
            pagos = Venta.objects.filter(client=client).order_by("-fecha")
            return render(
                request, "routines/pagos.html", {"client": client, "pagos": pagos}
            )
        else:
            raise Http404("No tiene permiso para acceder aquí")


def detalle_pago_view(request, id):
    user = None
    if request.user.is_authenticated:
        user = request.user
        if user.groups.filter(name="Clients").exists():
            client = Client.objects.get(user=request.user)
            pago = Venta.objects.get(id=id)
            detalle = DetalleVenta.objects.filter(pago=pago)
            return render(
                request,
                "routines/detalle-pago.html",
                {"user": user, "detalle": detalle},
            )
        else:
            raise Http404("No tiene permiso para acceder aquí")


@login_required
def catalog_view(request):
    user = None
    if request.user.is_authenticated:
        user = request.user
        if user.groups.filter(name="Clients").exists():
            client = Client.objects.get(user=request.user)
            productos = Producto.objects.filter(stock__gt=0)
            servicios = Servicio.objects.all()
            return render(
                request,
                "routines/catalogo.html",
                {"client": client, "productos": productos, "servicios": servicios},
            )
        else:
            raise Http404("No tiene permiso para acceder aquí")


@login_required
def detalle_producto_view(request, id):
    user = None
    if request.user.is_authenticated:
        user = request.user
        client = Client.objects.get(user=user)
        producto = get_object_or_404(Producto, id=id)
        return render(
            request,
            "routines/detalle-producto.html",
            {"client": client, "producto": producto},
        )


@login_required
def detalle_servicio_view(request, id):
    user = None
    if request.user.is_authenticated:
        user = request.user
        client = Client.objects.get(user=user)
        servicio = get_object_or_404(Servicio, id=id)
        desde = datetime.date.today()
        hasta = desde + relativedelta(months=1)
        return render(
            request,
            "routines/detalle-servicio.html",
            {"client": client, "desde": desde, "hasta": hasta, "servicio": servicio},
        )


@login_required
def perfil_alumno_view(request):
    user = None
    if request.user.is_authenticated:
        user = request.user
        if user.groups.filter(name="Clients").exists():
            client = Client.objects.get(user=user)
            ficha_medica = FichaMedica.objects.get(client=client)
            if request.method == "POST":
                form = ClientForm(request.POST, request.FILES)
                ficha = FichaForm(request.POST, instance=ficha_medica)
                foto = request.FILES["foto"]
                if form.is_valid() and ficha.is_valid():
                    fm = ficha.save(commit=False)
                    fm.altura = request.POST.get("altura")
                    fm.peso = request.POST.get("peso")
                    fm.sexo = request.POST.get("sexo")
                    fm.mutual = request.POST.get("mutual")
                    fm.observaciones = request.POST.get("observaciones")
                    fm.telefono_emergencia = request.POST.get("telefono_emergencia")
                    fm.client = client
                    fm.save()
                    perfil = form.save(commit=False)
                    perfil.user = request.user
                    perfil.nombre = request.POST.get("nombre")
                    perfil.apellido = request.POST.get("apellido")
                    perfil.dni = request.POST.get("dni")
                    perfil.telefono = request.POST.get("telefono")
                    perfil.domicilio = request.POST.get("domicilio")
                    perfil.profesor = client.profesor
                    perfil.id = client.id
                    perfil.save()
                    return redirect(index_view)
                else:
                    print(form.errors)
                    print(form.non_field_errors)
                    print(ficha.errors)
                    print(ficha.non_field_errors)
            else:
                form = ClientForm()
                ficha = FichaForm()
            return render(
                request,
                "routines/perfil-alumno.html",
                {"ficha": ficha, "form": form, "user": user, "client": client},
            )
        else:
            raise Http404("No tiene permiso para acceder aquí")


@login_required
def editar_perfil_profe_view(request):
    user = None
    if request.user.is_authenticated:
        user = request.user
        if user.groups.filter(name="Profesores").exists():
            profesor = Profesor.objects.get(user=user)
            if request.method == "POST":
                form = ProfesorForm(request.POST, request.FILES)
                foto = request.FILES["foto"]
                if form.is_valid():
                    perfil = form.save(commit=False)
                    perfil.user = request.user
                    perfil.nombre = request.POST.get("nombre")
                    perfil.apellido = request.POST.get("apellido")
                    perfil.telefono = request.POST.get("telefono")
                    perfil.domicilio = request.POST.get("domicilio")
                    perfil.id = profesor.id
                    perfil.save()
                    return redirect(index_view)
                else:
                    print(form.errors)
                    print(form.non_field_errors)
            else:
                form = ProfesorForm()
            return render(
                request,
                "routines/editar-perfil-profe.html",
                {"form": form, "user": user, "profesor": profesor},
            )
        else:
            raise Http404("No tiene permiso para acceder aquí")


@login_required
def comprar_view(request, id):
    user = None
    if request.user.is_authenticated:
        user = request.user
        if user.groups.filter(name="Clients").exists():
            client = Client.objects.get(user=user)
            producto = get_object_or_404(Producto, id=id)
            if request.method == "POST":
                form = VentaForm(request.POST)
                if form.is_valid():
                    venta = form.save(commit=False)
                    # commit=False tells Django that "Don't send this to database yet.
                    # I have more things I want to do with it."
                    venta.client = client  # Set the user object here
                    venta.monto = producto.precio
                    venta.fecha = datetime.datetime.now()
                    detalle_venta = DetalleVenta()
                    detalle_venta.cantidad = 1
                    detalle_venta.precio = producto.precio
                    detalle_venta.articulo = producto
                    venta.save()  # Now you can send it to DB
                    detalle_venta.pago = venta
                    detalle_venta.save()
                    venta.save()
                    producto.stock = producto.stock - 1
                    producto.save()

                    return redirect("pago_procesado")
            else:
                form = VentaForm()
            return render(
                request,
                "routines/comprar.html",
                {"form": form, "client": client, "producto": producto},
            )
        else:
            raise Http404("No tiene permiso para acceder aquí")


@login_required
def pagar_view(request, id):
    user = None
    if request.user.is_authenticated:
        user = request.user
        if user.groups.filter(name="Clients").exists():
            client = Client.objects.get(user=user)
            servicio = get_object_or_404(Servicio, id=id)
            pagos = Venta.objects.filter(client=client)
            for p in pagos:
                fechas = (
                    DetalleVenta.objects.filter(pago=p)
                    .exclude(hasta=None)
                    .order_by("hasta")
                )
                for f in fechas:
                    if f.hasta > datetime.date.today():
                        al_dia = True
                        return render(
                            request, "routines/pagar.html", {"f": f, "al_dia": al_dia}
                        )
                    else:
                        pass
            desde = datetime.date.today()
            hasta = desde + relativedelta(months=1)
            if request.method == "POST":
                form = VentaForm(request.POST)
                if form.is_valid():
                    venta = form.save(commit=False)
                    # commit=False tells Django that "Don't send this to database yet.
                    # I have more things I want to do with it."
                    venta.client = client  # Set the user object here
                    venta.monto = servicio.precio
                    venta.fecha = datetime.datetime.now()
                    detalle_venta = DetalleVenta()
                    detalle_venta.cantidad = 1
                    detalle_venta.precio = servicio.precio
                    detalle_venta.articulo = servicio
                    detalle_venta.desde = desde
                    detalle_venta.hasta = hasta
                    venta.save()  # Now you can send it to DB
                    detalle_venta.pago = venta
                    detalle_venta.save()
                    venta.save()

                    return redirect("pago_procesado")
            else:
                form = VentaForm()
            return render(
                request,
                "routines/pagar.html",
                {
                    "desde": desde,
                    "hasta": hasta,
                    "form": form,
                    "client": client,
                    "servicio": servicio,
                },
            )
        else:
            raise Http404("No tiene permiso para acceder aquí")


@login_required
def pago_procesado_view(request):
    user = None
    if request.user.is_authenticated:
        user = request.user
        client = Client.objects.get(user=user)
        return render(request, "routines/pago-procesado.html", {"client": client})


@login_required
def perfil_profe_view(request, id):
    user = None
    if request.user.is_authenticated:
        user = request.user
        if user.groups.filter(name="Clients").exists():
            client = Client.objects.get(user=user)
            profesor = get_object_or_404(Profesor, id=id)
            return render(
                request,
                "routines/perfil-profe.html",
                {"client": client, "profesor": profesor},
            )
        else:
            raise Http404("No tiene permiso para acceder aquí")


@login_required
def registro_ejercicio_view(request, r, e, d, s):
    user = None
    if request.user.is_authenticated:
        user = request.user
        if user.groups.filter(name="Clients").exists():
            client = Client.objects.get(user=request.user)
            re = RoutineEjercicio.objects.get(ejercicio=e, rutina=r, dia=d)
            sem = Semana.objects.get(id=s)
            try:
                reg = Registro.objects.get(
                    rutina_ejercicio__ejercicio=e,
                    rutina_ejercicio__rutina=r,
                    rutina_ejercicio__dia=d,
                    semana=s,
                )
            except Registro.DoesNotExist:
                reg = Registro.objects.create(rutina_ejercicio=re, semana=sem)
                form = SerieForm()
                for i in range(1, 5):
                    ser = Serie.objects.create(
                        numero=i, peso_levantado=0, repeticiones=0, registro=reg
                    )
                    ser.save()
                return render(
                    request,
                    "routines/registro-ejercicio.html",
                    {
                        "r": r,
                        "e": e,
                        "d": d,
                        "s": s,
                        "form": form,
                        "sem": sem,
                        "reg": reg,
                        "client": client,
                    },
                )
            else:
                if request.method == "POST":
                    if request.POST["completado"] == "True":
                        rf = RegistroForm(instance=reg)
                        rnew = rf.save(commit=False)
                        rnew.completado = True
                        rnew.save()
                        rc = RoutineClient.objects.get(client=client, actual=True)
                        return redirect(rutina_view, id=rc.id)
                    for i in range(1, 5):
                        ser = Serie.objects.get(
                            numero=request.POST["id_numero" + str(i)], registro=reg
                        )
                        f = SerieForm(instance=ser)
                        snew = f.save(commit=False)
                        snew.peso_levantado = request.POST["id_peso_levantado" + str(i)]
                        snew.repeticiones = request.POST["id_repeticiones" + str(i)]
                        snew.save()
                    return redirect(registro_ejercicio_view, r=r, e=e, d=d, s=s)
                form = SerieForm()
                return render(
                    request,
                    "routines/registro-ejercicio.html",
                    {
                        "r": r,
                        "e": e,
                        "d": d,
                        "s": s,
                        "form": form,
                        "sem": sem,
                        "reg": reg,
                        "client": client,
                    },
                )
        else:
            raise Http404("No tiene permiso para acceder aquí")
 """
