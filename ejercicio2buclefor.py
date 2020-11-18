
contrasena=input("introduzca una contraseña :")
contador=0
for i in range (len(contrasena)):

    if contrasena[i]==" ":
        contador=1

if len(contrasena)<8 or contador>0:
    print("contrasena erronea")
else:
    
    print("Contraseña OK")