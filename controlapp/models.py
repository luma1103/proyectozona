from django.db import models

from django.contrib import admin
from django.utils import timezone

class Evento(models.Model):
    nombre  =   models.CharField(max_length=100)
    fecha   = models.DateField()

    def __str__(self):
        return self.nombre

class Laboratorio(models.Model):
    nombre    = models.CharField(max_length=100)
    encargado = models.CharField(max_length=200)
    eventos   = models.ManyToManyField(Evento, through='Registro')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank = True, null= True)

    def __str__(self):
        return self.nombre

    def publish(self):
        self.published_date = timezone.now()
        self.save()

class Registro(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)

class RegistroInLine(admin.TabularInline):
    model = Registro
    extra = 1

class EventoAdmin(admin.ModelAdmin):
    inlines = (RegistroInLine,)

class LaboratorioAdmin (admin.ModelAdmin):
    inlines = (RegistroInLine,)
