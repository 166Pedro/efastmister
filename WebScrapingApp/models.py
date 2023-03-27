import requests
from bs4 import BeautifulSoup
from unidecode import unidecode

from EFastMisterApp.models import Jugadores

# Funcion que recoge todos los jugadores a partir de web scraping.
for i in range(1, 27):
    url = f"https://www.jornadaperfecta.com/jugadores/?pagina={i}"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    trJugadores = soup.find_all('tr', attrs={'itemtype': 'http://schema.org/Person'})
    divsPosicion = soup.find_all('div', class_='jugador-posicion')
    tdNombres = soup.find_all('td', attrs={'itemprop': 'name'})

    # Recorremos la lista de los td que contienen el nombre del jugador
    for td in tdNombres:
        # Creamos una variable que se llame nombre y le añadimos el texto dentro de cada td
        jugador = Jugadores()
        jugador.nombre = td.text

        # Conexion a la pagina concreta de cada jugador (PAGINA DONDE SE ENCUENTRAS SUS DATOS COMPLETOS)
        nombreUrl = unidecode(td.text.replace(" ", "-").replace(".", ""))
        urlJugador = f"https://www.jornadaperfecta.com/jugador/{nombreUrl.lower()}"
        pageJugador = requests.get(urlJugador)
        soupJugador = BeautifulSoup(pageJugador.content, "html.parser")
        divDatos = soupJugador.find('div', class_='jugador-datos-precio')
        divsDatos = divDatos.findAllNext('div')

        # Equipo real del jugador
        divEquipo = soupJugador.find('div', class_='player-team-shield')
        imgEquipo = divEquipo.findNext('img')
        jugador.equipoReal = imgEquipo.get('title')

        # Valor del jugador
        valor = int(divsDatos[0].text.replace(".", ""))
        jugador.valor = valor

        # Puntuacion del jugador
        puntuacion = soupJugador.find('div', class_='jugador-datos-cifra')
        jugador.puntuacion = puntuacion.text

        # Posicion del jugador
        posicion = soupJugador.find('div', class_='jp-pos')
        jugador.posicion = posicion.text

        jugador.save()
