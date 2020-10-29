import keyboard
import os

class Circle:
    coordinatedPrint = "o"

    def right(self):
        self.coordinatedPrint = " " + self.coordinatedPrint

    def down(self):
        self.coordinatedPrint += "\n" + self.coordinatedPrint

    def left(self):
        self.coordinatedPrint += "\b" + self.coordinatedPrint

    def getCoordinatedPrint(self):
        return self.coordinatedPrint
    
circleObj = Circle()

try:
    while True:
        os.system('cls')
        print(circleObj.getCoordinatedPrint())
        if keyboard.read_key() == 'd':
            circleObj.right()
        elif keyboard.read_key() == 's':
            circleObj.down()
        elif keyboard.read_key() == 'a':
            circleObj.left()
        
except KeyboardInterrupt:
    pass