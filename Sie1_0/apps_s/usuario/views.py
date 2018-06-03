# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect

from ..actividad.models import Actividad
from ..usuario.models import Usuario


def home(request):

    actividad = Actividad.objects.all()[:4]


    return render(request, 'principal.html', {'actividades': actividad})


def registro(request):

    user = Usuario()

    if request.method == 'POST':

        if 'telefono' in request.POST:

            user.telefono = request.POST['telefono']


            user.save()

        return redirect('/login/')

    return render(request, 'registroUsuario.html')