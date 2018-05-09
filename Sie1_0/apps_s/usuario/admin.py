from django.contrib import admin

# Register your models here.
from .models import Usuario, Rol, Permiso

admin.site.register(Usuario)
admin.site.register(Rol)
admin.site.register(Permiso)


