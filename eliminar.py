import sqlite3

bd=sqlite3.connect("contactos.db")
cursor=bd.cursor()
cedula=input("\nCedula: ")
sentencia="DELETE FROM contacto WHERE cedula =?"
cursor.execute(sentencia, (cedula,))
bd.commit()
bd.close()
print("Eliminado correctamente")