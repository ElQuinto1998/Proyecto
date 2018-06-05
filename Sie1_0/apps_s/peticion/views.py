# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from ..peticion.models import Peticion
from  ..usuario.models import Usuario
from django.contrib.auth.models import User
# Create your views here.

def blog_peticion(request):

    peticiones = Peticion.objects.all().order_by('-fecha')

    peticion = Peticion()


    if request.method == 'POST':


        peticion.titulo = request.POST['titulo']
        peticion.descripcion = request.POST['descripcion']

        peticion.save()

        return redirect('/peticiones/')

    return render(request, 'peticiones.html', {'peticiones': peticiones})

