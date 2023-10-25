import sqlite3

bd = sqlite3.connect("contactos.db")
cursor = bd.cursor()
cedula= input("\nCedula: ")
nombre= input("\nNombre: ")
apellido= input("\nApellido: ")
celular= input("\nCelular: ")
email= input("\nEmail: ")

sentencia = "INSERT INTO contacto(cedula, nombre, apellido, celular, email) VALUES (?,?,?,?,?)"
cursor.execute(sentencia, [cedula, nombre, apellido, celular, email])
bd.commit()
bd.close()
print("Guardado correctamente")