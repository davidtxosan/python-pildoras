import re

nombre1="Jara Lopez"
nombre2="Antonio Gomez"
nombre3="Lara Lopez"

#la funcion "match" siempre busca al COMIENZO de la cadena.
# comodin . significa que empiece a buscar resultado que empiecen por lo que hay a la derecha de ese punto.Ej:Lara,Sara,Jara..etc. "re.IGNORECASE" como tercer parametro para que no sea Case Sensitive.
if re.match(".ara", nombre3, re.IGNORECASE):

    print("hemos encontrado el nombre")
    
else:

    print("no lo hemos encontrado")

# la funcion "search" busca en TODA la longitud de la cadena
if re.search("Lopez", nombre1):

    print("hemos encontrado el nombre")
    
else:

    print("no lo hemos encontrado")




'''lista_nombres=['Ana',
                'Maria ',
                'Juan ',
                'Juan ',
                'David ',
                'Celia']'''

'''for usuario in lista_nombres:

      el metacaracter ^ significa "comienza por..." y $ significa "finaliza por..". el [] busca el criterio que esta dentro.
    if re.findall('^Juan', usuario)or re.findall('Sanchez$', usuario)or re.findall('[n]', usuario)or re.findall('Sanch[oe]',usuario):

    if re.findall('^[A-D]', usuario):
        print(usuario)'''

# print(textoEncontrado.start())
# print(textoEncontrado.end())
# print(textoEncontrado.span())

# print(len(re.findall(textoBuscar,cadena)))