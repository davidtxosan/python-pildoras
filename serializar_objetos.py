import pickle

class Vehiculos():

    def __init__(self, marca, modelo):

        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False
    def arrancar(self):

        self.enmarcha=True
    def acelerar(self):
        self.acelera=True

    def frenar(self):
        self.frena=True

    def estado(self):
        print("Marca:", self.marca,"\nModelo: ", self.modelo, "\nEn Marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)

coche1=Vehiculos("Mazda", "Mx5")
coche2=Vehiculos("Seat", "Leon")
coche3=Vehiculos("Renault", "Megane")

coches=[coche1, coche2, coche3]

fichero_coches=open("losCoches","wb")

pickle.dump(coches, fichero_coches)

fichero_coches.close()

del(fichero_coches)


fichero_coches_apertura=open("losCoches", "rb")

misCoches=pickle.load(fichero_coches_apertura)

for c in misCoches:

    print(c.estado())

