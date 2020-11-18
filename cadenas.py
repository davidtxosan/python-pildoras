"""#metodo upper para poner en mayusculas el string
nombreUsuario=input("introduzca su nombre: ")

print("El nombre es:" , nombreUsuario.upper())

#metodo lower para poner en minisculas el string
nombreUsuario=input("introduzca su nombre: ")

print("El nombre es:" , nombreUsuario.lower())

#metodo capitalize para poner en mayusculas la primera letra del string

nombreUsuario=input("introduzca su nombre: ")

print("El nombre es:" , nombreUsuario.capitalize())"""

#ejemplo practico para comprobar el funcionamiento de isdigit.
edad=input("introduce la edad: ")

while(edad.isdigit()==False):

    print("por favor,introduce un valor numerico")

    edad=input("introduce la edad: ")

if (int(edad)<18):
    print("No puede pasar")
else:
    print("puedes pasar")

