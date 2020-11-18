import sqlite3

miConexion = sqlite3.connect("GestionProductos")

miCursor = miConexion.cursor()


miCursor.execute('''
    CREATE TABLE PRODUCTOS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
    PRECIO INTEGER,
    SECCION VARCHAR(20))

''')

productos = [

    ("pelota", 20, "juguetería"),
    ("pantalón", 15, "confección"),
    ("pantalónes", 35, "confección"),
    ("destornillador", 17, "Ferretería"),
    ("jarrón", 43, "Cerámica"),

]
# Ponemos en el primer campo la palabra reservada NULL porque hemos puesto AUTOINCREMENT  al crear la tabla y el sistema crea un campo numerico que se incrementa solo.
miCursor.executemany("INSERT INTO PRODUCTOS VALUES(NULL,?,?,?)", productos)

miCursor.execute("SELECT * FROM PRODUCTOS")

#  creamos un bucle for para que la informacion se presente en pantalla un registro de bajo de otro. de lo contrario se puede prescindir del bucle for.

ListaProductos = miCursor.fetchall()

for producto in ListaProductos:

    print(producto)

miConexion.commit()

miConexion.close()
