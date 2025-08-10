#TODO: agregar base de datos real
#sqilite

import mysql.connector

# Credenciales de la base de datos
mydb = mysql.connector.connect(             #Establece conexion
  host="localhost",
  user="tu_usuario",
  password="tu_contraseña",
  database="nombre_de_tu_base_de_datos"
)

mycursor = mydb.cursor()

# Ejemplo de consulta
mycursor.execute("SELECT * FROM clientes")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

mydb.close()