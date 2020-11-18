"""nuestra primera ventana grafica.Si cambiamos la extension del archivo a .pyw al abrirla desde el explorador con el interprete de python no se abrira una ventana
de consola detras.
"""
from tkinter import * 

raiz=Tk()

#  poner titulo a la ventana
raiz.title("ventana de pruebas")

#  para evitar que se pueda redimensionar la ventana.booleano.se pùede poner 0 y 1 o "True" o "False"
#  raiz.resizable(0,0)

#  para cambiar el icono de la ventana por uno personalizado.La "r" es de ruta absoluta
raiz.iconbitmap(r"C:\Users\user\Desktop\python pildoras\graficos\icono.ico")

#  para cambiar el tamaño de la ventana
#raiz.geometry("650x350")

#  cambiar el color de fondo de la ventana
raiz.config(bg="blue")

raiz.config(cursor="hand2")

#creacion de un frame

miFrame=Frame()

miFrame.config(bg="red")

miFrame.config(width="650", height="350")

#empaquetado del frame para unirse a la raiz

miFrame.pack()

miFrame.config(bd=25)

miFrame.config(cursor="pirate")

miFrame.config(relief="sunken")

#  para que la ventana este a la escucha de eventos.Poner simepre en ultimo lugar
raiz.mainloop()