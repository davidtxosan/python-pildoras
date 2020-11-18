
#numeros=[17,24,35,49,9,41,69,78,98]

#print(list(filter(lambda numero_par:numero_par%2==0,numeros)))

class Empleado:

    def __init__(self,nombre, cargo, salario):

        self.nombre=nombre
        self.cargo=cargo
        self.salario=salario
    def  __str__(self):

        return "{} que trabaja como {} tiene un salario de {} €".format(self.nombre,self.cargo,self.salario)

listaEmpleados=[
Empleado("Juan","Director", 75000),
Empleado("Ana","Presidenta", 85000),
Empleado("Antonio","Adminsitrativo", 25000),
Empleado("Sara","Secretaria", 27000),
Empleado("Mario","Botones", 21000)

]

#la funcion filter necesita dos argumentos:el criterio con el que se filtra y el objeto,variable,lista etc a filtrar
salarios_altos=filter(lambda empleado: empleado.salario>50000, listaEmpleados)

for empleado_salario in salarios_altos:

    print(empleado_salario)
