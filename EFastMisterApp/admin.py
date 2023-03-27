from django.contrib import admin

from .models import *
# Register your models here.
admin.site.register(Comunidad),
admin.site.register(GestionComunidad),
admin.site.register(AccesoComunidades),
admin.site.register(Equipos),
admin.site.register(Jugadores)

