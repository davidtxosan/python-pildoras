"""uso de operadores AND y OR
print("programa de becas año 2017")
distancia_escuela=int(input("introduce la distancia a la escuela en km : "))
print(distancia_escuela)
numero_hermanos=int(input("introduce el numero de hermano en el centro : "))
print(numero_hermanos)

salario_familiar=int(input("introduce salario anual bruto : "))
print(salario_familiar)

if distancia_escuela>40 and numero_hermanos>2 or salario_familiar<=20000:

    print("usted tiene derecho a la beca") 
else:
    print("usted no tiene derecho a la beca.Mire las condiciones")"""
#uso de condicional IN

print("asignaturas optativas año 2017")
print("Asignaturas optativas: informatica grafica - Pruebas de software - Usabilidad y Accesibilidad")
opcion=input("elige la asignatura : ")
asignatura= opcion.lower()

if asignatura in("informatica grafica" ,"pruebas de software" , "usabilidad y accesibilidad"):

    print("Asignatura elegida : " + asignatura)
else:
    print("la asignatura no existe")