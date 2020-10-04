"""

Ejercicio 7. Hacer un programa que muestre todos los numeros impares
entre dos numeros que decida el usuario.

    @author: dK4RUX
"""

# Variables
primerNumero = int(input("Digite el primer numero: "))
segundoNumero = int(input("Digite el segundo numero: "))

for contador in range(primerNumero+1, segundoNumero):
    if contador%2 != 0:
        print(contador)