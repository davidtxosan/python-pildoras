'''area_triangulo=lambda base,altura:(base*altura)/2
triangulo1=area_triangulo(5,7)
triangulo2=area_triangulo(9,6)

print(triangulo1)
print(triangulo2)

# dos formas de hacerlo.una de ellas con un parametro y la segunda con dos parametros
al_cubo= lambda numero:numero**3
exponenteNumero= lambda numero,exponente:pow(numero,exponente)
print(al_cubo(3))
print(exponenteNumero(3,3))'''

destacar_valor=lambda comision:"¡{}! €".format(comision)

comision_Ana=15585

print(destacar_valor(comision_Ana))

