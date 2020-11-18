import sqlite3
miConexion = sqlite3.connect("Usuarios")

miCursor = miConexion.cursor()



miCursor.execute('INSERT INTO DATOSUSUARIOS VALUES("NULL","david", "sanchez", "dsad","camino coin 17","UFEIDSBFUISZ")')


miConexion.close()

