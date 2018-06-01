from django.db import models
from ..iglesia.models import Iglesia


class Actividad(models.Model):
    titulo = models.CharField(max_length=120, blank=True, null=True)
    descripcion = models.TextField()
    fecha = models.DateTimeField()
    ubicacion = models.CharField(max_length=120, blank=True, null=True)
    imagen = models.ImageField(upload_to='media/imagenes_actividad')
    iglesia = models.ForeignKey(Iglesia, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo


    class Meta:
        verbose_name = "Actividad"
        verbose_name_plural = "Actividades"
