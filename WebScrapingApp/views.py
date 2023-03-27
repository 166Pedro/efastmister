from django.http import HttpResponse

from EFastMisterApp.models import Jugadores


# Create your views here.

def index(request):
    jugador = Jugadores()
    # Aquí iría el código para asignar valores al jugador
    jugador.save()
    return HttpResponse("Jugador guardado en base de datos.")
