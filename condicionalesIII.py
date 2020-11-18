#uso de concatenacion de condicionales
edad=int(input("introduzca la edad : "))

if 0<edad<100:
    print("la edad es correcta")
else:
    print("edad incorrecta")

#ejemplo de evalucion de salario de varios empleados.concatenacion de condicionales 2
salario_presidente=int(input("introduzca el salario del presidente: "))
print("salario de presidente: " + str(salario_presidente))

salario_director=int(input("introduzca el salario del director: "))
print("salario de director: " + str(salario_director))

salario_jefe_area=int(input("introduzca el salario del jefe_area: "))
print("salario de jefe_area: " + str(salario_jefe_area))

salario_administrativo=int(input("introduzca el salario del administrativo: "))
print("salario de administrativo: " + str(salario_administrativo))

if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
    print("todo esta correcto")
else:
    print("algo falla en esta empresa")

