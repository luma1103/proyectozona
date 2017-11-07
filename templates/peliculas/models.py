# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib import admin

class Actor(models.Model):
    nombre = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()

    def _str_(self):
        return self.nombre

class Pelicula(models.Model):
    nombre    = models.CharField(max_length=60)
    anio      = models.IntegerField()
    actores   = models.ManyToManyField(Actor, through='Actuacion')

    def __str__(self):
        return self.nombre

class Actuacion (models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)

class ActuacionInLine(admin.TabularInline):
    model = Actuacion
#muestra un campo extra al momento de insertar, como indicación que se pueden ingresar N actores.
    extra = 1

class ActorAdmin(admin.ModelAdmin):
    inlines = (ActuacionInLine,)

class PeliculaAdmin (admin.ModelAdmin):
    inlines = (ActuacionInLine,)
