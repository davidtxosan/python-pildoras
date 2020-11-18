import pickle

class Persona:

    def __init__(self, nombre, genero, edad):

         self.nombre=nombre
         self.genero=genero
         self.edad=edad
         print("se ha creado una persona de nombre: ", self.nombre)
    
    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)

class ListaPersonas:

    personas=[]

    def __init__(self):

        listaDePersonas=open("ficheroExterno", "ab+")
        listaDePersonas.seek(0)

        try:        
            self.personas=pickle.load(listaDePersonas)
            print("se cargaron {} personas del fichero externo".format(len(self.personas)))
        except:
            print("el fichero esta vacio")
        finally:
            listaDePersonas.close
            del(listaDePersonas)

    def agregarPersonas(self, p):
        self.personas.append(p)
        self.guardarPersonasEnFicheroExterno()
    def mostrarPersonas(self):
        for p in self.personas:
            print(p)

    def guardarPersonasEnFicheroExterno(self):
        listaDePersonas=open("ficheroExterno", "wb")
        pickle.dump(self.personas, listaDePersonas)
        listaDePersonas.close()
        del(listaDePersonas)
    
    def mostrarInfoFicheroExterno(self):
        print("la informacion del fichero externo es la siguiente: ")
        for p in self.personas:
            print(p)



miLista=ListaPersonas()
persona=Persona("Ana", "Femenino", 20)
miLista.agregarPersonas(persona)
miLista.mostrarInfoFicheroExterno()

"""p=Persona("Sandra", "Femenino", 29)
miLista.agregarPersonas(p)
p=Persona("Antonio", "Masculino", 33)
miLista.agregarPersonas(p)
p=Persona("Ana", "Femenino", 20)
miLista.agregarPersonas(p)

miLista.mostrarPersonas()"""