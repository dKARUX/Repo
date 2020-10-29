"""
Programación orientada a objetos (POO o OOP)

Definir una clase Coche
"""

class Coche:

    # Atributos o propiedades (Variables)
    # Caracteristicas del Coche
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2

    # Métodos, son acciones que hace el objeto (Coche) (funciones)
    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self):
        return self.velocidad

    def setColor(self, entradaColor):
        self.color = entradaColor

    def getColor(self):
        return self.color
# fin definición clase

# Crear objetos / Instanciar la Clase
cocheObj = Coche()

cocheObj.acelerar()
cocheObj.acelerar()
print(cocheObj.getVelocidad())

cocheObj.frenar()
print(cocheObj.getVelocidad())

print(cocheObj.getColor())
cocheObj.setColor("Amarillo")
print(cocheObj.getColor())