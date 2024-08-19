import mysql.connector
from mysql.connector import Error

try:
    # Conectar con la BD en MySQL
    conexion = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='nombre_de_la_base_de_datos'  # Especifica el nombre de la base de datos
    )
    if conexion.is_connected():
        print("Conexión exitosa a la base de datos")
        
    # Crear un objeto de tipo cursor que se pueda reutilizar nuevamente
    cursor = conexion.cursor(buffered=True)
    
except Error as e:
    print(f"Ocurrió un error al intentar conectar con MySQL: {e}")
finally:
    if conexion.is_connected():
        cursor.close()
        conexion.close()
        print("Conexión cerrada.")

