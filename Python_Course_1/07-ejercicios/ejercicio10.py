"""
Ejercicio 10. El programa tiene que pedir la nota de 15 alumnos y sacar por pantalla cuantos han aprobado y cuantos han suspendido.

    @author: dK4RUX
"""

# Variables:
aprobados = 0
suspendidos = 0

contador = 0

while contador < 15:
    contador += 1
    calificacion = (int(input(f"Calificación para el alumno {contador}: ")))
    if calificacion <= 10 and calificacion >= 0:
        if calificacion < 6:
            suspendidos += 1
    
        if calificacion > 6:
            aprobados += 1
    else:
        contador -= 1
        print("Calificación invalida!")

print(f"Este ciclo escolar, la catidad de Alumnos que aprobaron fuerón {aprobados} mientras que la cantidad de suspendidos fueron {suspendidos}")