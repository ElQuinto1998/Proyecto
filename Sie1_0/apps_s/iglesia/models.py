# -*- coding: utf-8 -*-

from django.db import models

class Iglesia(models.Model):
    nombre = models.CharField(max_length=120, blank=True, null=True)



    def __str__(self):
        return self.nombre


    class Meta:
        verbose_name = "Iglesia"
        verbose_name_plural = "Iglesias"


class GrupoPequenio(models.Model):
    nombre = models.CharField(max_length=120, null=True, blank=True)
    numero_de_miembos = models.IntegerField(blank=True, null=True)
    iglesia = models.ForeignKey(Iglesia, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Grupo pequeño"
        verbose_name_plural = "Grupos pequeños"

