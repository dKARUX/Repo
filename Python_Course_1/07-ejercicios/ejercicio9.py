"""

Ejercicio 9, Hacer un programa que pida numeros alusuario indefinidamente hasta meter el nummero 111

   @author: dK4RUX
"""

#Variables
numero = 0

while numero != 111:
    numero = int(input("Inserte un numero: "))
    if numero == 111:
        print("Salida de bucle exitosa!")
        break