from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=30)
    contrasena = models.CharField(max_length=15)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

