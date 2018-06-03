from django.db import models
from django.contrib.auth.models import User
from ..iglesia.models import Iglesia

# Create your models here.
class Usuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=20)
    iglesia = models.ForeignKey(Iglesia, on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario.username

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

