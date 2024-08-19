from conexionBD import *
import datetime
class Servicio:
    def __init__(self,id_servicio, cliente, empleado, fecha, descripcion):
        self.id_servicio=id_servicio
        self.cliente=cliente
        self.empleado=empleado
        self.fecha=fecha
        self.descripcion=descripcion

    def crear(cliente,empleado,descripcion):
        try:
            fecha=datetime.datetime.now()
            cursor.execute(
                "insert into servicios values(null,%s,%s,%s,%s)",
                (cliente,empleado,fecha,descripcion)
            )
            conexion.commit()
            return True
        except:
            return False    
    @staticmethod
    def mostrar():
        try:
          cursor.execute(
            "select * from servicios ",
            
            
          )
          return cursor.fetchall()
        except:    
          return []

    @staticmethod
    def actualizar(id_servicio,cliente,empleado,descripcion):
       try:
         cursor.execute(
            "update servicios set cliente=%s, empleadp=%s, descripcion=%s, where id_servicio=%s",
            (cliente,empleado,descripcion,id_servicio)
         )
         conexion.commit()
         return True
       except: 
         return False
    
    @staticmethod
    def eliminar(id_servicio):
        try:
          cursor.execute(
            "delete from servicios where id_servicio=%s",
            (id_servicio,)
          ) 
          conexion.commit() 
          return True  
        except:    
          return False