# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from ..peticion.models import Peticion
# Create your views here.

def blog_peticion(request):
    peticiones = Peticion.objects.all().order_by()

    return render(request, 'peticiones.html', {'peticiones': peticiones})