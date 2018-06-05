from django.db import models
from django.contrib.auth.models import User
from ..iglesia.models import Iglesia

# Create your models here.
class Usuario(models.Model):
    usuario = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=20)
    iglesiaa = models.ForeignKey(Iglesia, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.telefono
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"


