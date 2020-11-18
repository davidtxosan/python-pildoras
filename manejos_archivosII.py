
from io import open

archivo_texto=open("archivo.txt","r+")#asi abrimos el archivo para lectura y escritura

#print(archivo_texto.read())

"""#uso del seek para cambiar el puntero de un archivo de texto de sitio
archivo_texto.seek(11)
#tambien se puede hacer pasando un parametro a la sentencia "read" con la diferencia de que lee solo los caracteres hasta la posicion que se introduce
print(archivo_texto.read(5))
print(archivo_texto.read())"""
"""para situar el puntero en la mitad del texto.
archivo_texto.seek(len(archivo_texto.read())/2)
print(archivo_texto.read())"""
#para añadir una linea en mitad del texto
lista_texto=archivo_texto.readlines()
lista_texto[1]="Esta es una linea incluida desde el exterior \n"
archivo_texto.seek(0)
archivo_texto.writelines(lista_texto)


archivo_texto.close()

