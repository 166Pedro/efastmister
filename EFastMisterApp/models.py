import uuid

from django.db import models

from UsersApp.models import *
# Create your models here.
class Comunidad(models.Model):
    nombre_comunidad = models.CharField(max_length=200, blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    administrador = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    miembros = models.ManyToManyField(User, related_name='miembros_comunidades')

    def __str__(self):
        return str(self.nombre_comunidad)

    class Meta:
        ordering = ['fecha_creacion']
