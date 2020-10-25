"""
Ejercicio 3. Programa que compruebe si una variable está vacia
y si está vacia, rellenarla con texto en minusculas y mostrarlo
en mayusculas.
"""
# Declarando variable del tipo string
variable = ""

# Evaluando si esta o no vacia
if variable == "":
    variable += 'texto nuevo'
else:
    print('Variable del tipo string no esta vacia')

# Imprimir contenido de variable y convertir a mayusculas
print(variable.upper())