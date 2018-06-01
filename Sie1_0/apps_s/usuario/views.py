# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

from ..actividad.models import Actividad


def home(request):
    actividad =  Actividad.objects.all()

    return render(request, 'principal.html', {'actividades': actividad})


def registro(request):
    return render(request, 'registroUsuario.html')