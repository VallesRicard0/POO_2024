import mysql.connector


try:
    # Conectar a la base de datos
    connection = mysql.connector.connect(
        host='localhost',  # Dirección del servidor MySQL
        database='nombre_bd',  # Nombre de la base de datos
        user='usuario',  # Usuario de MySQL
        password='contraseña'  # Contraseña del usuario
    )

    if connection.is_connected():
        print("Conexión exitosa a la base de datos")

        # Crear un cursor para ejecutar consultas
        cursor = connection.cursor()

        # Ejecutar una consulta simple
        cursor.execute("SELECT * FROM Clientes")

        # Obtener todos los registros
        registros = cursor.fetchall()

        print("Total de registros en la tabla 'Clientes':", cursor.rowcount)

        # Mostrar los registros
        for fila in registros:
            print(fila)

except Error as e:
    print(f"Error al conectar a MySQL: {e}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Conexión a MySQL cerrada")
