"""
Ejercicio 5.
Crear una lista con el contenido de esta tabla:
ACCION    AVENTURA    DEPORTES
--------------------------------------------
GTA        POKEMON    FIFA 21
COD        CRASH       PRO 21
PUBG       ZELDA      MOTO GP 21

Mostrar esta información ordenada
"""

tabla = [
    {
        "categoria": "ACCION",
        "juegos": ["GTA", "COD", "PUBG"]
    },
    {
        "categoria": "AVENTURA",
        "juegos": ["POKEMON", "CRASH", "ZELDA"]
    },
    {
        "categoria": "DEPORTES",
        "juegos": ["FIFA 21", "PRO 21", "MOTO GP 21"]
    }
]

for elemento in tabla:
    print(f'-------------------------------')
    print(f'----{elemento["categoria"]}----')
    print(f'-------------------------------')
    for subelemento in elemento["juegos"]:
        print(f'{subelemento}')