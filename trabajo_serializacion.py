#creacion de un archivo en formato binario con una lista en su interior
import pickle

lista_nombres=["Pedro", "Ana", "Maria", "Isabel"]

fichero_binario=open("lista_nombres", "wb")#wb=escritura binaria

pickle.dump(lista_nombres, fichero_binario)

fichero_binario.close()

del(fichero_binario)

#leer la informacion de ese archivo que hemos creado anteriormente

import pickle

fichero=open("lista_nombres", "rb")#lectura binaria

lista=pickle.load(fichero)

print(lista)



