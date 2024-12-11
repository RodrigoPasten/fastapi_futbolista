from fastapi import FastAPI, HTTPException

app = FastAPI()
futbolistas_leyendas = [
    {
        "nombre": "Pelé",
        "pais": "Brasil",
        "fecha_nacimiento": "1940-10-23",
        "clubes": ["Santos", "New York Cosmos"],
        "logros": ["3 Copas del Mundo (1958, 1962, 1970)", "2 Copas Libertadores"]
    },
    {
        "nombre": "Diego Maradona",
        "pais": "Argentina",
        "fecha_nacimiento": "1960-10-30",
        "clubes": ["Barcelona", "Napoli", "Boca Juniors"],
        "logros": ["Copa del Mundo 1986", "Campeón de la Serie A con Napoli"]
    },
    {
        "nombre": "Lionel Messi",
        "pais": "Argentina",
        "fecha_nacimiento": "1987-06-24",
        "clubes": ["FC Barcelona", "Paris Saint-Germain"],
        "logros": ["7 Balones de Oro", "4 Champions League", "Copa América 2021", "Mundial 2022"]
    },
    {
        "nombre": "Cristiano Ronaldo",
        "pais": "Portugal",
        "fecha_nacimiento": "1985-02-05",
        "clubes": ["Sporting CP", "Manchester United", "Real Madrid", "Juventus"],
        "logros": ["5 Balones de Oro", "5 Champions League", "Eurocopa 2016"]
    },
    {
        "nombre": "Zinedine Zidane",
        "pais": "Francia",
        "fecha_nacimiento": "1972-06-23",
        "clubes": ["Juventus", "Real Madrid"],
        "logros": ["Copa del Mundo 1998", "Eurocopa 2000", "3 Champions League como entrenador de Real Madrid"]
    },
{
        "nombre": "Johan Cruyff",
        "pais": "Países Bajos",
        "fecha_nacimiento": "1947-04-25",
        "clubes": ["Ajax", "Barcelona", "Feyenoord"],
        "logros": ["3 Balones de Oro", "Copa de Europa con Ajax", "Revolucionario del fútbol total"]
    },
    {
        "nombre": "Franz Beckenbauer",
        "pais": "Alemania",
        "fecha_nacimiento": "1945-09-11",
        "clubes": ["Bayern Múnich", "New York Cosmos"],
        "logros": ["Copa del Mundo 1974 como jugador", "Copa del Mundo 1990 como entrenador", "3 Copas de Europa con Bayern Múnich"]
    },
    {
        "nombre": "Alfredo Di Stéfano",
        "pais": "Argentina",
        "fecha_nacimiento": "1926-07-04",
        "clubes": ["River Plate", "Millonarios", "Real Madrid"],
        "logros": ["5 Copas de Europa con Real Madrid", "2 Balones de Oro", "Figura histórica del Real Madrid"]
    },
    {
        "nombre": "George Best",
        "pais": "Irlanda del Norte",
        "fecha_nacimiento": "1946-05-22",
        "clubes": ["Manchester United"],
        "logros": ["Balón de Oro 1968", "Copa de Europa 1968 con Manchester United"]
    },
    {
        "nombre": "Michel Platini",
        "pais": "Francia",
        "fecha_nacimiento": "1955-06-21",
        "clubes": ["Nancy", "Saint-Étienne", "Juventus"],
        "logros": ["3 Balones de Oro consecutivos (1983, 1984, 1985)", "Eurocopa 1984", "Copa de Europa 1985 con Juventus"]
    },
    {
        "nombre": "Lev Yashin",
        "pais": "Rusia",
        "fecha_nacimiento": "1929-10-22",
        "clubes": ["Dínamo Moscú"],
        "logros": ["Balón de Oro 1963", "Considerado el mejor portero de la historia"]
    },
    {
        "nombre": "Garrincha",
        "pais": "Brasil",
        "fecha_nacimiento": "1933-10-28",
        "clubes": ["Botafogo"],
        "logros": ["2 Copas del Mundo (1958, 1962)", "Considerado el mejor regateador de la historia"]
    },
    {
        "nombre": "Paolo Maldini",
        "pais": "Italia",
        "fecha_nacimiento": "1968-06-26",
        "clubes": ["AC Milan"],
        "logros": ["5 Champions League", "Figura histórica de AC Milan y del fútbol italiano"]
    },
    {
        "nombre": "Ronaldo Nazário",
        "pais": "Brasil",
        "fecha_nacimiento": "1976-09-22",
        "clubes": ["Cruzeiro", "Barcelona", "Inter de Milán", "Real Madrid", "AC Milan"],
        "logros": ["2 Copas del Mundo (1994, 2002)", "3 veces mejor jugador FIFA del año"]
    }
]


@app.get('/futbolistas')
async def futbolistas():
    return futbolistas_leyendas


@app.get('/futbolistas/{nombre}')
async def logros_futbolista(nombre: str):
    for futbolista in futbolistas_leyendas:
        if futbolista.get('nombre').casefold() == nombre.casefold():
            return futbolista['logros']


