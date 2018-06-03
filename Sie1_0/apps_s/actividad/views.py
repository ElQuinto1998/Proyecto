# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect

# Create your views here.
from ..actividad.models import Actividad
from ..iglesia.models import Iglesia


def blog_actividad(request):
    actividad = Actividad.objects.all().order_by('-fecha')

    return render(request, 'actividades.html', {'actividades': actividad})


def detalles_actividad(request, id):
    activ = Actividad.objects.get(id=id)

    return render(request, 'detalle_actividad.html', {'activ': activ})


def editar_actividad(request, id):
    actividad = Actividad.objects.get(id=id)
    iglesias = Iglesia.objects.all()

    if request.method == 'POST':

        actividad.titulo = request.POST['titulo']
        actividad.descripcion = request.POST['descripcion']
        #actividad.fecha = request.POST['fecha']
        actividad.ubicacion = request.POST['ubicacion']
        actividad.imagen = request.POST['imagen']
        #actividad.iglesia = request.POST['iglesia']

        actividad.save()

        return redirect('/actividades/')

    return render(request, 'form_actividad.html', {'actividad': actividad, 'iglesias': iglesias})


def eliminar_actividad(request, id):
    actividad = Actividad.objects.get(id=id)

    if request.method == 'POST':

        Actividad.delete(actividad)

        return redirect('/actividades/')

    return render(request, 'eliminar_actividad.html', {'actividad': actividad})


