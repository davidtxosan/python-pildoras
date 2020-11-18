#uso de una funcion clasica
def generaPares(limite):
    num=1
    
    miLista=[]

    while num<limite:

        miLista.append(num*2)

        num+=1
    return miLista

print(generaPares(10))

#uso de un generador,imprimiendo los 3 primeros elementos cuando se le invoca.mientras esta en estado de "suspension" ahorrando recursos y espacio.

def generaPares(limite):
    num=1
    
    while num<limite:

        yield num*2

        num+=1
devuelvePares=generaPares(10)

print(next(devuelvePares))
print("aqui podria ir mas codigo")

print(next(devuelvePares))
print("aqui podria ir mas codigo")

print(next(devuelvePares))
print("aqui podria ir mas codigo")

