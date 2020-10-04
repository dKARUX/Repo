"""

Ejercicio 4. Pedir dos numeros al usuario y hacer todas las
operaciones basicas de una calculadora y mostrarlo por pantalla

    @author: dK4RUX
"""

primerNumero = int(input("Inserte primer numero: "))
segundoNumero = int(input("Inserte segundo numero: "))

suma = primerNumero + segundoNumero
resta = primerNumero - segundoNumero
multiplicacion = primerNumero * segundoNumero
division = primerNumero / segundoNumero

print(f"La SUMA del numero {primerNumero} y el {segundoNumero} es igual a {suma}")
print(f"La RESTA del numero {primerNumero} y el {segundoNumero} es igual a {resta}")
print(f"La MULTIPLICACION del numero {primerNumero} y el {segundoNumero} es igual a {multiplicacion}")
print(f"La DIVISION del numero {primerNumero} y el {segundoNumero} es igual a {division}")