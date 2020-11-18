#uso de "range" y como concatenar el valor de una variable con strings.imprime el string + el contenido que está en ese momento entre las llaves.
for i in range(5):
    print(f"valor de la variable es:  {i}")
#como decir desde que elemento comenzar,en que elemento terminar y el espacio entre numeros

for i in range(2,100,2):
    print(f"el valor del numero es : {i}" )

#funcion "length".ponemos "len" para decirle al bucle for que lea la longitud del texto que introducimos por teclado.luego el bucle "for" va a recorrer cada posicion.

valido =False

email=input("introduce tu email: ")
for i in range (len(email)):

    if email[i]=="@":
        valido=True

if valido:
    print("el mail tiene una arroba")
else:
    print("el email no tiene una arroba")