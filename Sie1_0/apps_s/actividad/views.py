# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

# Create your views here.
from ..actividad.models import Actividad


def blog_actividad(request):
    actividad = Actividad.objects.all()

    return render(request, 'actividades.html', {'actividades': actividad})


def editar_actividad(request, id):
    actividad = Actividad.objects.get(id=id)

    return render(request, 'editar_actividad.html', {'actividad': actividad})


def eliminar_actividad(request, id):
    actividad = Actividad.objects.get(id=id)

    return render(request, 'eliminar_actividad.html', {'actividad': actividad})


def detalles_actividad(request, id):
    activ = Actividad.objects.get(id=id)

    return render(request, 'detalle_actividad.html', {'activ': activ})