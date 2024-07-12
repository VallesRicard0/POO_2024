from conexionBD import *
try:
   micursor=conexion.cursor()

   sql="update clientes set tel='6181112233' where id='4'"
   micursor.execute(sql)
   conexion.commit()
except:
   print(f"Ocurrio un error")
else:
   print(f"Registro Actualizado Correctamente")