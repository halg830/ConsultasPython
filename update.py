import sqlite3
cnx = sqlite3.connect("contactos.db")
cursor = cnx.cursor()
cursor.execute("UPDATE contacto SET nombre = 'Pancha' WHERE nombre = 'Lina'")
cnx.commit()
cnx.close()