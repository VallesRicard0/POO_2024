import mysql.connector
import os

# Lee la contraseña desde una variable de entorno
password = os.environ.get('MYSQL_PASSWORD')

try:
    # Conectar con la BD en MySQL
    conexion = mysql.connector.connect(
        host='localhost',
        user='root',
        password=password,
        database='hotel23'
    )
    # Crear un objeto de tipo cursor que se pueda reutilizar nuevamente
    cursor = conexion.cursor(buffered=True)
except mysql.connector.Error as err:
    print(f"Error al conectar a la base de datos: {err}")
finally:
    # Cierra la conexión
    if conexion:
        conexion.close()