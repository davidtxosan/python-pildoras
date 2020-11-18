#bucle for con una lista

for i in ["primavera", "verano" ,1 ,2]:
    print(i)
#bucle con salto de linea.imprime un "hola" por cada elemento de la lista.
for i in ["pildoras", "Informaticas",3]:
    print("hola", end=" ")
#imprimir contando letras de un string.imprime un "hola" por cada letra que tenga el string
    """for i in "juan@pildorasinformaticas.es" :
        print("hola", end=" ")"""

#comprobar si una direccion de email es correcta o no(que tenga una @ Y ADEMAS TENGA UN .)

contador=0
Miemail = input("introduzca su email : ")
for i in Miemail:
    
    if(i=="@" or i=="."):

        contador=contador+1

if contador==2:
    print("email es correcto")
else: 
    print("el mail no es correcto")

