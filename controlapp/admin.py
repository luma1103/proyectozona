from django.contrib import admin
from controlapp.models import Evento, EventoAdmin, Laboratorio, LaboratorioAdmin

#Registramos nuestras clases principales.
admin.site.register(Evento, EventoAdmin)
admin.site.register(Laboratorio, LaboratorioAdmin)
