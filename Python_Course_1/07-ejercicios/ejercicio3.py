"""

Ejercicio 3. Escribir un programa que muestre los cuadrados
(un numero multiplicado por si mismo) de los 60 primeros numeros
naturales. Resolverlo con FOR y con WHILE

    @author: dK4RUX
"""

contador = 0

while contador <= 60:
    print(contador*contador)
    contador += 1

print("#########################################")

contador = 0

for contador in range(0,61):
    print(contador*contador)