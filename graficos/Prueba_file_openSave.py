from tkinter import *
from tkinter import filedialog

root=Tk()
# Funcion de una ventana emergente con el explorador de windows para elegir un fichero para abrirlo.
def abreFichero():
    #-----------busqueda con filtros------------
    fichero=filedialog.askopenfilename(title="Abrir", initialdir="C:/",filetypes=(("Ficheros de texto", "*.txt"),
    ("ficheros ejecutables", "*.exe"),("todos los ficheros", "*.*")))
    # la sentencia print nos va a inmprimir en consola la ruta del archivo que hemos abierto,NO SU CONTENIDO.
    print(fichero)

Button(root, text="Abrir fichero",command=abreFichero).pack()


root.mainloop()