#creacion de un diccionario
midiccionario={"Alemania":"Berlin", "Francia":"Paris", "España":"Madrid"}
print(midiccionario["Francia"])
#Añadir elementos al diccionario o modificar un elemento
midiccionario["Italia"]="Lisboa"
print(midiccionario)
#eliminar un elemento del diccionario
del midiccionario["Francia"]
print(midiccionario)
#diccionario con varios tipos de elementos
midiccionario={"Alemania":"Francia", 23:"Jordan", "Mosqueteros":3}
print(midiccionario)
#añadir avalores a una tupla desde un diccionario
mitupla=["España", "Francia", "Reino Unido", "Alemania"]
midiccionario={mitupla[0]:"Madrid", mitupla[1]:"Paris", mitupla[2]:"Londres", mitupla[3]:"Berlin"}
print(midiccionario)
#para acceder a un elemento
print(midiccionario["Francia"])
#meter una tupla dentro de un diccionario
midiccionario={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "anillos":[1991,1992,1993,1996,1997,1998]}
#imprimir solo unos de los valores
print(midiccionario["anillos"])
#guardar un diccionario dentro de otro diccionario teniendo este una tupla dentro
midiccionario={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "anillos":{"temporadas":[1991,1992,1993,1996,1997,1998]}}
print(midiccionario)
#metodo keys para sacar las claves del diccionario
print(midiccionario.keys())
#imprimir los valores del diccionario
print(midiccionario.values())
#imprimir la longitud o numero de items del diccionario
print(len(midiccionario))



