import sqlite3
cnx=sqlite3.connect("contactos.db")
cursor=cnx.cursor()
cursor.execute("DELETE FROM contacto WHERE nombre = 'Raul'")
cnx.commit()