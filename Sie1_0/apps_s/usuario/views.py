# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

from ..actividad.models import Actividad


def home(request):
<<<<<<< HEAD
    actividad =  Actividad.objects.all()
=======
    actividad = Actividad.objects.all()[:4]
>>>>>>> master

    return render(request, 'principal.html', {'actividades': actividad})


def registro(request):
    return render(request, 'registroUsuario.html')