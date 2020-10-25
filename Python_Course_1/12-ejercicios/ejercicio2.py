"""
Ejercicio 2. Escribir un programa que añada valores a una lista
mientras que su longitud sea menor a 20 y luego mostrar la lista
Plus: usar while y for, entrada de datos por teclado
"""
# Creando lista para la colección de valores
listaValoresWhile = []
listaValoresFor = []

# Declarando Iterador
indice = 0

# Añadiendo datos con bucle tipo while
while indice < 20:
    listaValoresWhile.append(int(input(f'Escriba un nuevo valor para indice {indice} de la lista...')))
    indice += 1

print(listaValoresWhile)

# Añadiendo datos con bucle tipo for
for i in range(0,20):
    listaValoresFor.append(int(input(f'Escriba un nuevo valor para indice {i} de la lista...')))

print(listaValoresFor)