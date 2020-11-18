from tkinter import *

raiz= Tk()

miFrame=Frame(raiz, width=1200, height=600)

miFrame.pack()

# creacion de la variable que luego utilizaremos en la función para que se agregue al campo "nombre" al darle al botón "Enviar".
minombre=StringVar()

#-----------elementos del formulario---------------------------------

# asociamos la variable al campo nombre

cNombre=Entry(miFrame, textvariable=minombre)

cPass=Entry(miFrame)

cApellido=Entry(miFrame)

cuadroEdad=Entry(miFrame)

TextoComentario=Text(miFrame, width=36, height=15)

barra=Scrollbar(miFrame, command=TextoComentario.yview)

barra.grid(row=4, column=2, sticky="nsew")

TextoComentario.config(yscrollcommand=barra.set)

cNombre.grid(row=0, column=1,pady=10,padx=10)

cNombre.config(fg="red", justify="center")

cApellido.grid(row=1,column=1,pady=10,padx=10)

cuadroEdad.grid(row=2,column=1,pady=10,padx=10)

cPass.grid(row=3,column=1,pady=10,padx=10)

cPass.config(show="#")

TextoComentario.grid(row=4,column=1, pady=10,padx=10)



#  forma resumida de hacerlo

nombreLabel=Label(miFrame, text="Nombre: ").grid(row=0, sticky="w",pady=10,padx=10)

PassLabel=Label(miFrame, text="Password: ").grid(row=3, sticky="w",pady=10,padx=10)

#  forma completa y mas larga

ApellidosLabel=Label(miFrame, text="Apellidos: ")

ApellidosLabel.grid(row=1, sticky="w",pady=10,padx=10)

DireccionLabel=Label(miFrame, text="Dirección: ")

DireccionLabel.grid(row=2, sticky="w",pady=10,padx=10)

ComentariosLabel=Label(miFrame, text="Comentarios: ")

ComentariosLabel.grid(row=4, sticky="w",pady=10,padx=10)

# creacion de una funcion para que al darle al botón "Enviar", se rellene el campo "nombre" con el texto que hemos puesto.
def codigoBoton():

    Boton1.set("1")

botonEnvio=Button(raiz, text="Enviar", command=codigoBoton)

botonEnvio.pack()



raiz.mainloop()