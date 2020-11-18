from tkinter import *

root=Tk()

miFrame=Frame(root, width=500, height=400)

miFrame.pack()

miImagen=PhotoImage(file="mouse.gif")#solo de ejemplo,la imagen "mouse.gif" no existe

Label(miFrame, image=miImagen)




root.mainloop()