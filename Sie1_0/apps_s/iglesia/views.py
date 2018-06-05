# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from ..iglesia.models import Iglesia

# Create your views here.
def iglesia(request):
    iglesias = Iglesia.objects.all()

    return render(request, 'iglesias.html', {'iglesias': iglesias})


def detalle(request, id_iglesia):

    iglesias = Iglesia.objects.all()

    igle = Iglesia.objects.get(id=id_iglesia)

    return render(request, 'iglesias.html', {'iglesias': iglesias, 'igle': igle})


def buscar(request):

    existe = ''
    iglesiaBuscada = Iglesia()

    if request.method == 'POST':

        print('*********************entre**************')

        busqueda = request.POST['iglesia']

        try:
            iglesiaBuscada = Iglesia.objects.get(nombre=busqueda)
            pk = iglesiaBuscada.id

            if iglesiaBuscada:

                return render(request, 'iglesias.html', {'iglesiaB': iglesiaBuscada, 'pk': pk})

        except iglesiaBuscada.DoesNotExist:

            existe = 'No hay iglesia con ese nombre'
            return render(request, 'iglesias.html', {'existe': existe})

    return render(request, 'buscarIglesia.html')