"""i=1
while i<=10:
    print("ejecucion numero: "+ str(i))
    i=i+1
print("termino la ejecucion del programa")"""

#ejemplo de posible bucle infinito
"""edad=int(input("introduce la edad: "))
while edad<0 or edad>100:
    print("la edad no es correcta,vuelve a intentarlo")
    edad=int(input("introduce la edad : "))
print("tienes: "+ str(edad)+ " "+"años")"""
import math
print("programa de calculo de raiz cuadrada")
numero=int(input("introduce un numero por favor: "))
intentos=0
while numero<0:
    print("no se puede hallar raices cuadradas de numeros negativos.")
    if intentos==2:
        print("has consumido el limite de intentos.El programa ha finalizado")
        break;
    numero=int(input("introduce un numero por favor: "))
    if numero<0:
        intentos=intentos+1
if intentos<2:
    print("la raiz cuadrada de: "  + str(numero)+ " es: " + str(math.sqrt(numero)))