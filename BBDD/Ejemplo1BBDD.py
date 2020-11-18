import sqlite3

miConexion=sqlite3.connect("PrimeraBase")

miCursor=miConexion.cursor()

# miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")

#miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALÓN', 15, 'DEPORTES')")

"""variosProductos=[

    ("Camiseta", 10, "Deportes"),
    ("Jarrón", 10, "Cerámica"),
    ("Camión", 10, "Juguetería")

]
# forma de insertar varios registros a la vez.S poenen tantos ? como campos tienen los registros.

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", variosProductos)"""

miCursor.execute("SELECT * FROM PRODUCTOS")

ListaProductos=miCursor.fetchall()

for producto in ListaProductos:

    print("nombre del Articulo: ", producto[0], "nombre de la sección: ", producto[2])

miConexion.commit()

miConexion.close()