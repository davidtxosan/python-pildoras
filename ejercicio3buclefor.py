email=input("introduzca el email: ")
contadorarroba=0
contadorpunto=0
for i in range(len(email)):

    if email[i]=="@":
        contadorarroba=contadorarroba+1
    if email[i]==".":
        contadorpunto=1
if contadorpunto==0 or contadorarroba!=1:
    print("email incorrecto")

else:
    print("email correcto")

