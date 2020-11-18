numero=int(input("introduce un numero positivo: "))
suma=0
while numero>0:
    suma=suma+numero
    print("la suma de los numeros introducidos es: " + str(suma))
    numero=int(input("introduce otro numero: "))
print("el numero ",numero,"no es positivo.Programa finalizado.")