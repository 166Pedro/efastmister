import uuid

from django.core.validators import MaxValueValidator, MinValueValidator
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


class GestionComunidad(models.Model):
    comunidad = models.ForeignKey(
        Comunidad,
        on_delete=models.CASCADE
    )
    futbolistasMercado = models.IntegerField(validators=[
        MaxValueValidator(20),
        MinValueValidator(5)
    ])
    pagosClausulas = models.BooleanField()
    presupuestoInicial = models.IntegerField(null=True)
    dineroPorPunto = models.IntegerField(null=True)
    intercambioJugadores = models.BooleanField()

    def __str__(self):
        return str(self.comunidad)

    class Meta:
        ordering = ['id']


class AccesoComunidades(models.Model):
    codigoAcceso = models.CharField(max_length=200, blank=True, null=True)
    comunidad = models.ForeignKey(
        Comunidad,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.codigoAcceso)

    class Meta:
        ordering = ['id']

class Equipos(models.Model):
    nombre = models.CharField(max_length=200, blank=True, null=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    comunidad = models.ForeignKey(
        Comunidad,
        on_delete=models.CASCADE,
        null=True
    )
    puntosTotales = models.IntegerField(null=True)


    def __str__(self):
        return str(self.nombre)

    class Meta:
        ordering = ['id']

class Jugadores(models.Model):
    nombre = models.CharField(max_length=200, blank=True, null=True)
    posicion = models.CharField(max_length=200, blank=True, null=True)
    puntuacion = models.IntegerField(null=True)
    valor = models.IntegerField(null=True)
    equipoReal = models.CharField(max_length=200, blank=True, null=True)
    equipo = models.ForeignKey(
        Equipos,
        on_delete=models.CASCADE,
        null=True
    )
    libre = models.BooleanField()

    def __str__(self):
        return str(self.nombre)

    class Meta:
        ordering = ['id']


