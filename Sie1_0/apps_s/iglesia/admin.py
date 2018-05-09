from django.contrib import admin

# Register your models here.
from .models import Iglesia, GrupoPequenio

admin.site.register(Iglesia)
admin.site.register(GrupoPequenio)