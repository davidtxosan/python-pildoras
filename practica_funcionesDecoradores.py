def funcion_decoradora(funcion_parametro):

    def funcion_interior(*args,**kwargs):

        # acciones adicionales que decoran

        print("a continuacion realizaremos el calculo: ")
        # el parametro *args significa que puede recibir un numero indeterminado de parametros.El parametro **kwargs se pone cuando se pasan clave:valor al llamar a una funcion.(ver funcion "potencia")
        funcion_parametro(*args,**kwargs)

        # acciones adicionales que decoran

        print("ya se ha realizado el calculo: ")

    return funcion_interior


@funcion_decoradora
def  suma(num1,num2,num3):


    print(num1+num2+num3)


def resta(num1,num2,num3):
    

    print(num1-num2-num3)

@funcion_decoradora
def potencia(base,exponente):

     print("la potencia de ", base ," a la ", exponente, "es: ", pow(base,exponente))

potencia(base=2,exponente=3)

suma(7,5,8)

resta(22,10,8)