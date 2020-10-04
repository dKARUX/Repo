"""

Ejercicio 5. Hacer un programa que muestre todos los numeros entre dos numeros que diga el usuario.

    @author: dK4RUX
"""

# Variables
primerNumero = int(input("Digite el primer numero: "))
segundoNumero = int(input("Digite el segundo numero: "))

contador = 0

if primerNumero < segundoNumero:
    for contador in range (primerNumero+1, segundoNumero):
        print(contador)
else:
    print("El primer numero debe ser menor al segundo numero, por favor intente de nuevo")