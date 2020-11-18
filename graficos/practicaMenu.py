from tkinter import *
from tkinter import messagebox

root=Tk()

#---------------------------funciones de ventanas emergentes-----------------------------------------

def infoAdicional():

    messagebox.showinfo("texto cabecera", "texto a rellenar")

def avisoLicencia():

    messagebox.showwarning("licencia","producto sin licenciar, piratilla!")

def avisoSalida():

# ventana emergente con valor de si o no.(o "aceptar" y "cancelar").la primera coge "yes"y "no" y la segunda "true" o "false".

    #  valor=messagebox.askquestion("salir", "realmente deseas salir?")
    valor=messagebox.askokcancel("salir", "realmente deseas salir?")
    if valor==True:
        root.destroy()

def avisoCerrar():

    valor=messagebox.askretrycancel("reintentar","no es posible cerrar la aplicacion con el documento sin guardar.")
    if valor==True:
        root.destroy()

barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)

# -----------------elementos principales de la barra Menú--------------------

archivoMenu=Menu(barraMenu,tearoff=0)
archivoEdicion=Menu(barraMenu,tearoff=0)
archivoHerramientas=Menu(barraMenu,tearoff=0)
archivoAyuda=Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edición", menu=archivoEdicion)
barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)

#---------------------insercion de un submenu--------------------------

archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Abrir")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar", command=avisoCerrar)
archivoMenu.add_command(label="Salir", command=avisoSalida)

archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")

# --------opcion de submenu con ventana emergente de AVISO
archivoAyuda.add_command(label="Licencia", command=avisoLicencia)

# -------opcion de submenu con ventana emergente de INFORMACION------
archivoAyuda.add_command(label="Acerca de..", command=infoAdicional)


root.mainloop()