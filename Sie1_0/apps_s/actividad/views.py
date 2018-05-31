# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

# Create your views here.
from ..actividad.models import Actividad


def blog_actividad(request):
    actividad = Actividad.objects.all()

    return render(request, 'actividades.html', {'actividades': actividad})


def editar_actividad(request):



    print('++++++++++Holii++++++++++');

    return render(request, 'editar_actividad.html')