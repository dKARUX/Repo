"""
Ejercicio 8. Cuanto es el X por cientro de X numero.

   @author: dK4RUX
"""

# Variables
numero = int(input("Introduce el numero del cual desea saber su valor porcentual: "))
valorPorciento = int(input("Introduce el porcentaje a calcular: %"))
transPorciento = valorPorciento / 100
resultado = numero * transPorciento

print(f"El resultado es: {resultado}")