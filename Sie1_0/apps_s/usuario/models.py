from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=120, blank=True, null=True)
    correo = models.EmailField()


    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

