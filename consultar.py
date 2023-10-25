import sqlite3
cnx = sqlite3.connect("contactos.db")
cursor = cnx.cursor()
cursor.execute("SELECT * FROM contacto")
result = cursor.fetchall()
print(result)
for registro in result:
    print("Cedula:", registro[0], "Nombre: ", registro[1], "Apellido: ", registro[2], "Celular: ", registro[3],  "Email: ", registro[4])

cursor = cnx.cursor()
cursor.execute("SELECT celular FROM contacto WHERE cedula = '1234567890'")
result = cursor.fetchone()
print("Celular de cedula 1234567890: ", result[0])