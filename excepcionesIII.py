
#creacion de una excepcion
"""def evaluaEdad(edad):
    if edad<0:
        raise ZeroDivisionError("edad no permitida")
    if edad>20:
        return"eres muy joven"
    elif edad<40:
        return"Eres joven"
    elif edad<65:
        return "Eres maduro"
    elif edad<100:
        return"cuidate..."
print(evaluaEdad(-18))"""

#creacion de otra excepcion
import math

def calculaRaiz(num1):

    if num1<0:
        raise ValueError ("el numero no puede ser negativo")

    else:
        return math.sqrt(num1)

op1=(int(input("introduce un numero: ")))

try:

    print(calculaRaiz(op1))

except ValueError as ErrorDeNumeroNegativo:

    print(ErrorDeNumeroNegativo)

print("programa terminado")