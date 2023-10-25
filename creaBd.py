import sqlite3
con = sqlite3.connect("contactos.db")
cursor = con.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS contacto
                 (cedula TEXT PRIMARY KEY NOT NULL,
                 nombre TEXT NOT NULL,
                 apellido TEXT,
                 celular TEXT NOT NULL,
                 email TEXT)
                 """)
con.commit()
con.close()