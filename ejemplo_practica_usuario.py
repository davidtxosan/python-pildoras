class Persona():

 def __init__(self):

  self.__nombre=""

  self.__sexo=""

  self.__edad=0

  self.__nacionalidad=""



 def introduce_nombre(self):

  self.__nombre=input("Introduce tu nombre, por favor: ")



 def introduce_sexo(self):

  while True:

   sexo=input("Introduce tu sexo H/M: ")

   sexo1=sexo.upper()

   if sexo1=="H":

    self.__sexo="Hombre"

    break

   elif sexo1=="M":

    self.__sexo="Mujer"

    break

   else:

    print("Datos introducidos no validos. Si eres hombre escribe una H y si eres una mujer escribe una M")



 def introduce_edad(self):

  while True:

   try:

    edad=int(input("Introduce tu edad: "))

    break

   except ValueError:

    print("Debes introducir números, no letras.")

  if edad<=0:

   while True:

    edad=int(input("La edad no puede ser negativa.\nIntroduce una edad positiva:"))

    if edad>0:

     break

  self.__edad=edad

 def introduce_nacionalidad(self):

  self.__nacionalidad=input("Introduce tu nacionalidad: ")

   

 def datos_Persona(self):

  print("Nombre: " + self.__nombre)

  print("Sexo: " + self.__sexo)

  print("Edad: " + str(self.__edad))

  print("Nacionalidad: " + self.__nacionalidad)

###############################################################

persona1=Persona()

persona1.introduce_nombre()

persona1.introduce_sexo()

persona1.introduce_edad()

persona1.introduce_nacionalidad()

persona1.datos_Persona()