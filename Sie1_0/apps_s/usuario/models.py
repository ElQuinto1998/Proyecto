from django.db import models
from django.contrib.auth.models import User
from ..iglesia.models import Iglesia

# Create your models here.
class Usuario(models.Model):
    usuario = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    fecha_nacimiento = models.DateField(null=True)
    telefono = models.CharField(max_length=20)
    iglesiaa = models.ForeignKey(Iglesia, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return "%s \\ %s \\ %s \\ %s" % (
            self.usuario, self.fecha_nacimiento, 
            self.telefono, self.iglesiaa
        )

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"


