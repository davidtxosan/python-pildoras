from tkinter import *
from tkinter import messagebox
import sqlite3

root=Tk()

miFrame=Frame(root,width=1000, height=600)
miFrame.pack()

barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)


#---------------------PARTE LOGICA------------------------------

#---------------botones del menu superior------------------

def avisoSalida():
    valor=messagebox.askokcancel("Salir", "¿Desea salir de la aplicación?")
    if valor==True:
        root.quit()

def avisoLicencia():
    messagebox.showwarning("licencia","producto sin licenciar")

def infoPrograma():
   messagebox.showinfo("version 1.0", "programa de prueba Pildoras Informaticas")

def CreacionBaseDatos():
    miConexion=sqlite3.connect("Usuarios")
    miCursor=miConexion.cursor()
    try:
        miCursor.execute('''
            CREATE TABLE DATOSUSUARIOS (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE_USUARIO VARCHAR(50),
            PASSWORD VARCHAR(50),
            APELLIDOS VARCHAR(50),
            DIRECCION VARCHAR(80),
            COMENTARIOS VARCHAR(100))
             ''' )
        messagebox.showinfo("BBDD", "BBDD creada con exito")
    except:
        messagebox.showwarning("¡Atención!", "La BBDD ya existe")

    miConexion.close()

def BorradoCamposFormulario():
    cNombre.delete(0,END)
    cApellido.delete(0,END)
    cPassword.delete(0,END)
    cDireccion.delete(0,END)
    cComentarios.delete(1.0, END)
def crear():
    miConexion=sqlite3.connect("Usuarios")
    miCursor=miConexion.cursor()
# ver videos de PHP/mySQL del 47 al 53 de pildoras informaticas para evitar la inyeccion de datos SQL

    datos=miNombre.get(),miApellidos.get(),miPassword.get(),miDireccion.get(),cComentarios.get("1.0",END)
    miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,?,?,?,?,?)",(datos))
    
    miConexion.commit()

    messagebox.showinfo("BBDD", "registro insertado con exito")

def modificar():
    miConexion=sqlite3.connect("Usuarios")
    miCursor=miConexion.cursor()

    datos=miNombre.get(),miApellidos.get(),miPassword.get(),miDireccion.get(),cComentarios.get("1.0",END)
    miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO=?, APELLIDOS=?, PASSWORD=?,DIRECCION=?,COMENTARIOS=?" + 
     "WHERE ID=" + miID.get(),(datos))
    miConexion.commit()

    messagebox.showinfo("BBDD", "registro actualizado con exito")
def leer():
    miConexion=sqlite3.connect("Usuarios")
    miCursor=miConexion.cursor()
    miCursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID=" + miID.get())
    elUsuario=miCursor.fetchall()
   

    for usuarios in elUsuario:

        miID.set(usuarios[0])
        miNombre.set(usuarios[1])
        miApellidos.set(usuarios[2])
        miPassword.set(usuarios[3])
        miDireccion.set(usuarios[4])
        cComentarios.insert(1.0,usuarios[5])

    miConexion.commit()

def  BorradoRegistros():
    miConexion=sqlite3.connect("Usuarios")
    miCursor=miConexion.cursor()
    miCursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID=" + miID.get())

    miConexion.commit()

    messagebox.showinfo("BBDD" , "Registro borrado con exito")

#  -------------------PARTE VISIBLE-----------------------------

#-------------Elementos principales de la barra de Menú---------

BBDDMenu=Menu(barraMenu,tearoff=0)
BorrarMenu=Menu(barraMenu,tearoff=0)
CRUDMenu=Menu(barraMenu,tearoff=0)
AyudaMenu=Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label="BBDD",menu=BBDDMenu)
barraMenu.add_cascade(label="Borrar",menu=BorrarMenu)
barraMenu.add_cascade(label="CRUD",menu=CRUDMenu)
barraMenu.add_cascade(label="Ayuda",menu=AyudaMenu)
#  -----------------Elementos del submenu------------------------

BBDDMenu.add_command(label="Conectar",command=CreacionBaseDatos)
BBDDMenu.add_command(label="Salir",command=avisoSalida)

BorrarMenu.add_command(label="Borrar Campos",command=BorradoCamposFormulario)

CRUDMenu.add_command(label="Crear",command=crear)
CRUDMenu.add_command(label="Leer",command=leer)
CRUDMenu.add_command(label="Modificar",command=modificar)
CRUDMenu.add_command(label="Borrar",command=BorradoRegistros)

AyudaMenu.add_command(label="Acerca de...",command=infoPrograma)
AyudaMenu.add_command(label="Licencia",command=avisoLicencia)

#-----------elementos del formulario------------------------------

miID=StringVar()
miNombre=StringVar()
miApellidos=StringVar()
miPassword=StringVar()
miDireccion=StringVar()


cId=Entry(miFrame,textvariable=miID)
cId.grid(row=0,column=1,padx=10,pady=10,sticky="w")

cNombre=Entry(miFrame,textvariable=miNombre)
cNombre.grid(row=1,column=1,padx=10,pady=10,sticky="w")

cApellido=Entry(miFrame,textvariable=miApellidos)
cApellido.grid(row=2,column=1,padx=10,pady=10,sticky="w")

cPassword=Entry(miFrame,textvariable=miPassword)
cPassword.grid(row=3,column=1,padx=10,pady=10,sticky="w")
cPassword.config(show="#")

cDireccion=Entry(miFrame,textvariable=miDireccion)
cDireccion.grid(row=4,column=1,padx=10,pady=10,sticky="w")

cComentarios=Text(miFrame,width=25,height=10)
cComentarios.grid(row=5,column=1,padx=10,pady=10,sticky="w")
BarraAreaTexto=Scrollbar(miFrame,command=cComentarios.yview)
cComentarios.config( yscrollcommand=BarraAreaTexto.set)
BarraAreaTexto.grid(row=5,column=2, sticky="nsew")

#---------------text de las etiquetas---------------------------

IDLabel=Label(miFrame,text="ID: ").grid(row=0,sticky="w",column=0,padx=10,pady=10)
NombreLabel=Label(miFrame,text="Nombre: ").grid(row=1,sticky="w",column=0,padx=10,pady=10)
ApellidosLabel=Label(miFrame,text="Apellidos: ").grid(row=2,sticky="w",column=0,padx=10,pady=10)
PasswordLabel=Label(miFrame,text="Password: ").grid(row=3,sticky="w",column=0,padx=10,pady=10)
DireccionLabel=Label(miFrame,text="Direccion: ").grid(row=4,sticky="w",column=0,padx=10,pady=10)
ComentariosLabel=Label(miFrame,text="Comentarios: ").grid(row=5,sticky="w",column=0,padx=10,pady=10)

#---------------botones inferiores--------------------------------

miFrameInferior=Frame(root)
miFrameInferior.pack()
botonCreate=Button(miFrameInferior,text="Create",command=crear).grid(row=0,column=0,sticky="w",padx=10,pady=10)
botonRead=Button(miFrameInferior,text="Read",command=leer).grid(row=0,column=1,sticky="w",padx=10,pady=10)
botonUpdate=Button(miFrameInferior,text="Update",command=modificar).grid(row=0,column=2,sticky="w",padx=10,pady=10)
botonDelete=Button(miFrameInferior,text="Delete",command=BorradoRegistros).grid(row=0,column=3,sticky="w",padx=10,pady=10)

root.mainloop()