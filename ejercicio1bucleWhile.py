numero1=int(input("introduce el primer numero: "))
numero2=int(input("introduce un numero mayor que " +str(numero1) + ":"))

while numero1<numero2:
    numero1 = numero2
    numero2=int(input("introduce un numero mayor que " +str(numero1) + ":"))
    
print(
    print(numero2, "no es mayor que", str(numero1)))
    
