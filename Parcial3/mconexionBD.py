import mysql.connector
try:
#Conectar con la BD MySQL
    conexion=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='bd_python'
)

except Exception as e:
    #print(f"error: {e}")
    #print(f"Fue tipo de error: {type(e).__name__}")
    print(f"Ocurrio un problema con el servidor por favor intentalo mas tarde")
#verificar la conexion a la BD
else:
    print(f"Se creo la conexion con la BD exitosamente")
    