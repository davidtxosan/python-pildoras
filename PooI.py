# creacion de una clase con sus propiedades
class Coche():
    #creacion de metodo Constructor
    def __init__(self):
        #los dos guiones bajos__ encapsulan la propiedad o variables para que no se pueda modificar desde FUERA  de la clase.(Se Encapsula)
        self.__largoChasis=250
        self.__anchoChasis=120
        self.__ruedas=4
        self.__enmarcha=False

#comportamientos de la clase(metodos)
    def arrancar(self,arrancamos):
        self.__enmarcha=arrancamos
        if (self.__enmarcha):
            chequeo=self.__chequeo_interno()

        if(self.__enmarcha and chequeo):
            return "El coche esta en marcha"
        elif(self.__enmarcha and chequeo==False):
            return "Algo ha ido mal en el chequeo. no podemos arrancar"


        else:
            return"El coche esta parado"
        
    def estado(self):
        print("El coche tiene ", self.__ruedas, "ruedas.Un ancho de ", self.__anchoChasis, " y un largo de ", self.__largoChasis)
    #metodo encapsulado para que solo se pueda solicitar desde dentro de la clase,es decir que el metodo "chequeo interno"solo se solicite cuando el coche va a arrancar.
    def __chequeo_interno(self):
        print("realizando chequeo interno")
        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"

        if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
            
            return True
        else:
            return False

        
#creacion de una instancia o ejemplar u objeto
miCoche=Coche()
#las dos lineas de abajo ya no son necesarias al haber creado un comportamiento en la clase que hace la misma funcion
"""print("el largo del coche es: ", miCoche.anchoChasis)
print("El coche tiene ", miCoche.ruedas, " ruedas")"""

print(miCoche.arrancar(True))

miCoche.estado()

print("-----------a continuacion creamos el segundo objeto-------------------------------------------------------------------------------------------")

miCoche2=Coche()
#las dos lineas de abajo ya no son necesarias al haber creado un comportamiento en la clase que hace la misma funcion
"""print("el largo del coche es: ", miCoche2.anchoChasis)
print("El coche tiene ", miCoche2.ruedas, " ruedas")"""

print(miCoche2.arrancar(False))


miCoche2.estado()


