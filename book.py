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
        "logros": ["7 Balones de Oro", "4 Champions League", "Copa América 2021"]
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


