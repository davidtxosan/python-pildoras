#funcion "continue" hace que el bucle se salte una iteracion con el parametro indicado y pase a la siguiente.
for letra in "Python":
    if letra=="h":
        continue
    print("viendo la letra: " + letra)

#bucle for para contar letras de una frase con "continue"para que no cuente espacios en blanco
nombre="Pildoras Informaticas"
contador=0
for i in nombre:
    if i==" ":
        continue
    contador+=1
print(contador)

#funcion "pass" devuelve un "null".se utiliza para implementar,por ejemplo ,una clase y terminar de programar despues.
class MiClase:
    pass # para implementar mas tarde
# funcion "else".ESTE ELSE NO PERTENECE AL "IF" sino al FOR.
email=input("introduzca un email: ")
for i in email:
    if i =="@":
        arroba=True
        break;
else:
    arroba=False
print(arroba)
