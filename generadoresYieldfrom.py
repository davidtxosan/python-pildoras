#utilizacion de un bucle for anidado en otro bucle for y el uso de "yield" para extraer datos del subelemento(las 2 primeras letras del primer elemento)
def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        #for subElemento in elemento:
            yield from elemento
ciudades_devueltas=devuelve_ciudades("Madrid","Barcelona", "Bilbao","Valencia")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
 