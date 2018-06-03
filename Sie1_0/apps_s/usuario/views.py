from django.shortcuts import render

# Create your views here.
from ..actividad.models import Actividad


def home(request):
    actividad = Actividad.objects.all()[:4]

    return render(request, 'principal.html', {'actividades': actividad})