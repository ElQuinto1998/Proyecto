from django.db import models

# Create your models here.

class Rol(models.Model):
    nombre = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Rol"
        verbose_name_plural = "Roles"


class Permiso(models.Model):
    nombre = models.CharField(max_length=120, null=True, blank=True)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Permiso"
        verbose_name_plural = "Permisos"


class Usuario(models.Model):
    nombre = models.CharField(max_length=120, blank=True, null=True)
    correo = models.EmailField()
    rol = models.OneToOneField(Rol, primary_key=True, on_delete=models.CASCADE)


    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
