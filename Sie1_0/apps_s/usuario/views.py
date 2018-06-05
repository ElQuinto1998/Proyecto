# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from ..actividad.models import Actividad
from ..usuario.models import Usuario
from  ..iglesia.models import Iglesia


def home(request):

    actividad = Actividad.objects.all()[:3]


    return render(request, 'home.html', {'actividades': actividad})


def registro(request):

    iglesias = Iglesia.objects.all()

    user = Usuario()

    if request.method == 'POST':

        nombre = request.POST['nombre']
        apellidos = request.POST['apellidos']
        correo = request.POST['correo']
        contrasenia = request.POST['contraseña']

        if User.objects.filter(username=nombre):
            return render(request, 'registroUsuario.html', {'iglesias': iglesias, 'existe': 'El usuario ya existe'})

        user.usuario = User.objects.create_user(nombre,correo, contrasenia, last_name=apellidos)
        user.usuario.save()

        user.telefono = request.POST['telefono']
        ig = request.POST['iglesia']
        user.iglesiaa = Iglesia.objects.get(id=ig)

        user.save()

        return redirect('/login/')

    return render(request, 'registroUsuario.html', {'iglesias': iglesias})