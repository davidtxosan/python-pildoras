class persona():

    def __init__(self, nombre, edad, Lugar_residencia):

        self.nombre=nombre

        self.edad=edad

        self.lugar_residencia=Lugar_residencia

    def descripcion(self):

        print("Nombre: ", self.nombre, "Edad: ", self.edad, " Residencia:  ", self.lugar_residencia)

class empleado(persona):

    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):

        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)

        self.salario=salario

        self.antiguedad=antiguedad
    def descripcion(self):
        super().descripcion()
        print("salario: ", self.salario,"antiguedad: ", self.antiguedad)

Manuel=empleado(1500, 15, "Manuel", 55, "Colombia")

Manuel.descripcion()
#Uso de la función  isinstace para averiguar si un objeto es instancia de una clase determinada.Devuelve "True" si el objeto pertenece a la clase que se pregunta.
print(isinstance(Manuel, empleado))

