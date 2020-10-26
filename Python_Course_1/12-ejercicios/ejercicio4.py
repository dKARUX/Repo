"""
Ejercicio 4.
Crear un script que tenga 4 variables, una lista, un string,
un entero y un booleano y que imprima un mensaje
segun el tipo de dato de cada variable. Usar funciones
"""
# Funcion para identificar tipo de dato de la variable de entrada
def identificadorDeTipoDeDato(variableEntrada):
    tipoDeDato = type(variableEntrada)
    
    if tipoDeDato == list:
        resultado = "Lista"
    elif tipoDeDato == str:
        resultado = "Cadena de texto"
    elif tipoDeDato == int:
        resultado = "Numero Entero"
    elif tipoDeDato == bool:
        resultado = "Booleano"

    return resultado

# Declaración de variables
variableLista = ["Hola", "Mundo", 1]
variableString = "Esto es un texto"
variableEntero = 27
variableBooleano = True

# Impresión de salido de funcion identificadora de tipo de dato
print(identificadorDeTipoDeDato(variableLista))
print(identificadorDeTipoDeDato(variableString))
print(identificadorDeTipoDeDato(variableEntero))
print(identificadorDeTipoDeDato(variableBooleano))
