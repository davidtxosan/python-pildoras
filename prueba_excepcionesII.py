def divide():

    try:

        op1=(float(input("introduce el primer numero: ")))
        op2=(float(input("introduce el segundo numero: ")))

        print("la division es:" + str(op1/op2))


    except ValueError:
    
        print("El valor introducido es erroneo")

    except ZeroDivisionError:
        print("no se puede dividir entre cero")

        #poner una excepcion general,sin tener que especificar el tipo de error.Tiene que ir sola o al final del resto de excepciones para que funcione.
    except:
        print("ha ocurrido un error general")
        
    #todo lo que este dentro de la clausula "finally" se va a ejecutar SI O SI
    finally:

        print("calculo finalizado")

print("calculo finalizado")

divide()