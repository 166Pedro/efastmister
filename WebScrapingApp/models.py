from django.db import models
from EFastMisterApp.models import Jugadores
from bs4 import BeautifulSoup
import requests
import cssutils
from csv import writer


# Create your models here.

HEADERS = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}

URL = "https://www.comuniazo.com/comunio-apuestas/jugadores"
r = requests.get(url=URL, headers=HEADERS)

responseCss = requests.get(URL)

soup = BeautifulSoup(r.text, 'html.parser')

# Estilos del documento
styles = soup.head.style.string

# Parseamos la hoja de estilos con cssutils
sheet = cssutils.parseString(styles)

# Sacamos la tabla de los jugadores del HTML
table = soup.find("table")

# Sacamos los tbody que hay dentro de la tabla
tbodys = table.findAll("tbody")

with open('jugadores.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Nombre']
    thewriter.writerow(header)

    # Recorremos cada tbody y sacar todos los tr dentro de cada uno
    for tbody in tbodys:
        trs = tbody.findAllNext("tr")

        # Recorremos cada tr para sacar todos los td dentro de cada uno
        for tr in trs:
            tds = tr.findAllNext("td")
            tdNombre = tr.findNext("div", class_="player")
            tdPosicion = tr.findNext("span")

            # Creo la variable del nuevo jugador para que le vaya seteando los datos correspondientes
            # poco a poco

            jugador = Jugadores()

            # Comprobamos si el td contiene un div dentro con la clase player, asi sabremos que ese td es el del nombre
            if tdNombre:
                td = tdNombre.parent.parent

                # Sacamos el nombre del jugador
                nombre = tdNombre.text.strip()
                jugador.nombre = nombre

            if tdPosicion:
                td = tdPosicion.parent
                clasesPosicion = "." + tdPosicion['class'][1]

                rule = sheet.cssRules[0]
                if rule.selectorText == clasesPosicion:
                    # Obtenemos el valor del estilo "content"
                    content = rule.style.content
                    print(content)

                # jugador.posicion = posicion


            # thewriter.writerow(posicion)
            # puntuacion = tds[1].text.strip()
            # valor = tds[7].text.strip()

            # jugador.posicion = posicion
            # jugador.puntuacion = puntuacion
            # jugador.valor = valor
            # datos = [nombre, posicion, puntuacion, valor]


            # Guardamos el jugador en base de datos
            # jugador.save()
