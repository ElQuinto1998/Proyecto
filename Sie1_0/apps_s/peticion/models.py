from django.db import models
#from Sie1_0.apps_s.usuario.models import Usuario

# Create your models here.
class Peticion(models.Model):
    titulo = models.CharField(max_length=120, blank=True, null=True)
    descripcion = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    #usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Peticion"
        verbose_name_plural = "Peticiones"
