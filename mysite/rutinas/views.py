from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def index_view(request):
    return render(request, "rutinas/inicio-alumno.html")
