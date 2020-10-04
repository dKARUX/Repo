"""

Ejercicio 6. Mostrar todas las tablas de multiplicar del 1 al 10.
Mostrando el titulo de la table y luego las multiplicaciones de 1 al 10.

    @author: dK4RUX
"""

for primerContador in range (0,10):
    primerContador += 1
    print("Tabla del ", primerContador)
    for segundoContador in range(1,11):
        print(primerContador, " x ", segundoContador, " = ", primerContador*segundoContador)
        segundoContador += 1