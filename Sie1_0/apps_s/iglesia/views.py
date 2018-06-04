# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from ..iglesia.models import Iglesia

# Create your views here.
def iglesia(request):
    iglesias = Iglesia.objects.all()

    return render(request, 'iglesias.html', {'iglesias': iglesias})