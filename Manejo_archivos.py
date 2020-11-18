#ejemplo de como crear un archivo externo,escribir informacion en el y cerrarlo para que deje de estar en la memoria.

#importación del paquete io
from io import open

#creacion de una variable con la accion de crear(o usar) un archivo de texto con permisos de escritura.
archivo_texto=open("archivo2.txt","w")

#creacion de una variable con un texto dentro
frase="Estupendo dia para jugar a la xbox el martes"

#se usa el metodo "write" en la variable "archivo_texto" para introducir el texto de de la variable "frase"(que a su vez se intoduce en el archivo "archivo2.txt")
archivo_texto.write(frase)

#se cierra en memoria la variable "archivo_texto" con el metodo "close"
archivo_texto.close()

#otro ejemplo ,pero abriendo un archivo en modo lectura.
from io import open

archivo_texto=open("archivo2.txt","r")

texto=archivo_texto.read()

archivo_texto.close()

print(texto)#un ultimo ejemplo usando la sentencia readlines para que guarde la informacion en una lista


from io import open

archivo_texto=open("archivo2.txt","r")

lineas_texto=archivo_texto.readlines()

archivo_texto.close()

#accediendo a una parte de la lista
print(lineas_texto[0])

#abrir un archivo externo para agregar informacion

from io import open

archivo_texto=open("archivo2.txt","a")

archivo_texto.write("\n y pasarselo genial")

archivo_texto.close()

