"""def evaluacion(nota):
    valoracion="aprobado"
    if nota<5:
        valoracion="suspenso"
    else:
        valoracion="aprobado"
    return valoracion

print(evaluacion(4))"""
#introduccion de datos por teclado(input)SIEMPRE LO CONSIDERA UN STRING.EL metodo INPUT admite parametros 

nota_alumno=input()

def evaluacion(nota):
    valoracion="aprobado"
    if nota<5:
        valoracion="suspenso"
    else:
        valoracion="aprobado"
    return valoracion

print(evaluacion(int(nota_alumno)))

