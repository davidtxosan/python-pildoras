class Coche():

    def desplazamiento(self):
        print("me desplazo utilizando cuatro ruedas")

class Moto():

    def desplazamiento(self):
        print("me desplazo utilizando dos ruedas")

class Camion():

    def desplazamiento(self):

        print("me desplazo utilizando seis ruedas")

#forma de crear instancias de las clases e imprimir el metodo "desplazamiento" en cada una de ellas.
miVehiculo=Moto()

miVehiculo.desplazamiento()

miVehiculo2=Coche()

miVehiculo2.desplazamiento()

miVehiculo3=Camion()

miVehiculo3.desplazamiento()

#mismo objetivo pero usando el POLIMORFISMO:

def desplazamientoVehiculo(vehiculo):

    vehiculo.desplazamiento()

miVehiculo=Coche()

desplazamientoVehiculo(miVehiculo)
