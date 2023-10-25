import sqlite3
cnx = sqlite3.connect("contactos.db")
#CURSOR para comunicarse con la base de datos
cursorbd = cnx.cursor()
cursorbd.execute("""CREATE TABLE IF NOT EXISTS contacto
                 (cedula TEXT PRIMARY KEY,
                 nombre TEXT NOT NULL,
                 apellido TEXT,
                 celular TEXT NOT NULL,
                 email TEXT)
                 """)
cnx.commit()
cnx.close()