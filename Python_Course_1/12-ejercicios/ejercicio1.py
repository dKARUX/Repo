"""
Ejercicio 1. Hacer un programa que tenga una lista
de 8 numeros enteros y haga lo siguiente:
- Recorrer la lista y mostrarla (Hacer funcion que recorra listas de numeros y devuelva un string)
- Ordenarla y mostrarla
- Mostrar su longitud
- Buscar algun elemento (que el usuario pida por teclado)
"""

# Crear la lista de 8 numeros enteros
print('Creando la lista de 8 numeros enteros...')
lista = [32, 12, 43, 67, 11, 99, 102, 2]
print('Lista creada...')
print(lista)

# Recorrer la lista y mostrarla
print('Recorriendo la lista y mostrandola...')
print('Mostrando lista recorrida...')
for i in lista:
    print(i)

# Hacer funcion que recorra listas de numeros y devuelva un string
print('Creando funcion que recorra listas de numeros y devuelva un string...')
def recorrerLista(listaEntrada):
    cadenaSalida = ""
    for i in listaEntrada:
        cadenaSalida += str(i)
    
    return cadenaSalida

print('Devolviendo string generado...')
print(recorrerLista(lista))

# Ordenarla y mostrarla
print('Ordenando lista...')
print('Creando funcion para ordenamiento de listas...')
def ordenarLista(listaEntrada):
    for i in range(0,len(listaEntrada)):
        ordenarListaHelper(listaEntrada)
    return ordenarListaHelper(listaEntrada)

print('Creando funcion de ayuda para la funcion de ordenamiento de listas...')
def ordenarListaHelper(listaEntrada):
    for i in range(0, len(listaEntrada)-1):
        if listaEntrada[i] > listaEntrada[i+1]:
            temp = listaEntrada[i+1]
            listaEntrada[i+1] = listaEntrada[i]
            listaEntrada[i] = temp
    return listaEntrada

print('Mostrando lista ordenada...')
print(ordenarLista(lista))

# Mostrar su longitud
print('Monstrando longitud de la lista...')
print(len(lista))

# Buscar algun elemento (que el usuario pida por teclado)
print('Creando la solicitud para la entrada por teclado de la decisión proxima del usuario...')
seleccionElementoLista = int(input('Elija el elemento de la lista a mostrar...'))
print(lista[seleccionElementoLista])