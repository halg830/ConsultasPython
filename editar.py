import sqlite3

from tabulate import tabulate

bd=sqlite3.connect("contactos.db")
cursor=bd.cursor()
cursor.execute("SELECT * FROM contacto")
result = cursor.fetchall()
print(result)
table=[["Cedula", "Nombre", "Apellido", "Celular", "Email"]]
for (registro) in result:
    table.insert(1, registro)

print(tabulate(table))

cursor = bd.cursor()
campo=input("\nEscoja el campo a modificar: ")
cedula=input("\nCedula: ")
editar=input(f"\n{campo}: ")
if(campo=="todo"):
    sentencia="UPDATE contacto SET "
sentencia=f"UPDATE contacto SET nombre WHERE cedula =?"
cursor.execute(sentencia, (editar, cedula,))
cursor.execute(f"SELECT * FROM contacto WHERE cedula = '{cedula}'")
result = cursor.fetchall()
print("Editado correctamente", result)
bd.commit()
bd.close()


