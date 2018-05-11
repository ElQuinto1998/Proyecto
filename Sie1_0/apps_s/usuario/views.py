from django.shortcuts import render

# Create your views here.
from ..actividad.models import Actividad


def home(request):
    actividad = Actividad.objects.all()

    return render(request, 'principal.html', {'actividades': actividad})