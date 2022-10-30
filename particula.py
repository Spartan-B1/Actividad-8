from cmath import sqrt
import math

class Particula:
    def __init__(self, id = 0.0, origen_X= 0.0, origen_Y= 0.0, 
                destino_X= 0.0, destino_Y= 0.0, velocidad= 0.0, 
                red= 0.0, green= 0.0, blue= 0.0):
        self.__id = str(id)
        self.__origen_x = str(origen_X)
        self.__origen_y = str(origen_Y)
        self.__destino_x = str(destino_X)
        self.__destino_y = str(destino_Y)
        self.__velocidad = str(velocidad)
        self.__red = str(red)
        self.__green = str(green)
        self.__blue = str(blue)
        #self.__distancia = (distancia_euclidiana(origen_X, origen_Y, destino_X, destino_Y))
    
    def __str__(self):
        return(
            'ID: ' + self.__id + '\n' +
            'Origen X: ' + self.__origen_x + '\n' +
            'Origen Y: ' + self.__origen_y + '\n' +
            'Destino X: ' + self.__destino_x + '\n' +
            'Destino Y: ' + self.__destino_y + '\n' +
            'Velocidad: ' + self.__velocidad + ' M/S \n' +
            'Rojo: ' + self.__red + '\n' +
            'Verde: ' + self.__green + '\n' +
            'Azul: ' + self.__blue + '\n'
            #'Distancia: ' + self.__distancia +  ' M \n' 
            )

    @property
    def id(self):
        return self.__id

    @property
    def origenX(self):
        return self.__origen_x

    @property
    def origenY(self):
        return self.__origen_y

    @property
    def destinoX(self):
        return self.__destino_x

    @property
    def destinoY(self):
        return self.__destino_y

    @property
    def velocidad(self):
        return self.__velocidad

    @property
    def red(self):
        return self.__red

    @property
    def green(self):
        return self.__green

    @property
    def blue(self):
        return self.__blue
    
    @property
    def distancia(self):
        ox = float(self.__origen_x)
        oy = float(self.__origen_y)
        dx = float(self.__destino_x)
        dy = float(self.__destino_y)
        return repr(sqrt(pow((ox - dx), 2) + pow((oy - dy), 2)))
    
    def to_dict(self):
        return {
            "id": self.__id,
            "origen_X": self.__origen_x,
            "origen_Y": self.__origen_y,
            "destino_X": self.__destino_x,
            "destino_Y": self.__destino_y,
            "velocidad": self.__velocidad,
            "red": self.__red,
            "green": self.__green,
            "blue": self.__blue
        }
