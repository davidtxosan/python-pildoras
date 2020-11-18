from tkinter import *

root = Tk()

root.title = ("Ejemplo")

playa = IntVar()
montagna = IntVar()
turismoRural = IntVar()

def imprimir():

    opcionEscogida = ""

    if (playa.get()==1):

        opcionEscogida+=" playa"
    
    if(montagna.get()==1):

        opcionEscogida+=" Montaña"

    if(turismoRural.get()==1):

        opcionEscogida+=" Turismo rural"

    etiqueta.config(text=opcionEscogida)

#  no me funciona la imgen si pongo una ruta relativa
foto = PhotoImage(file="C:/Users/user/Desktop/python pildoras/graficos/avion.png")

Label(root, image=foto).pack()

frame=Frame(root)
frame.pack()

Label(frame, text="elige destinos: ", width=70).pack()

# onvalue: casilla verificada, offvalue:casilla no verificada
Checkbutton(frame, text="PLaya" ,variable=playa, onvalue=1, offvalue=0, command=imprimir).pack()
Checkbutton(frame, text="Montaña", variable=montagna, onvalue=1,offvalue=0 ,command=imprimir).pack()
Checkbutton(frame, text="Turismo rural", variable=turismoRural, onvalue=1,offvalue=0, command=imprimir).pack()

etiqueta=Label(frame)

etiqueta.pack()

root.mainloop()
