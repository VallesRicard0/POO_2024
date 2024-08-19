from conexionBD import *

class Plan:
    def __init__(self, id_planes,nombre_plan,precio_plan):
        self.id_planes=id_planes
        self.nombre_plan=nombre_plan
        self.precio_plan=precio_plan

    def crear(nombre_plan,precio_plan):
        try:
          cursor.execute(
            "insert into planes values(null,%s,%s);",
            (nombre_plan,precio_plan)
          )
          conexion.commit()
          return True
        except:
          return False
    @staticmethod
    def mostrar():
        try:
          cursor.execute(
            "select * from planes",
            
          )
          return cursor.fetchall()
        except:    
          return []

    @staticmethod
    def actualizarNombre(id_planes,nombre_plan):
       try:
         cursor.execute(
            "update planes set nombre_plan=%s where id_planes=%s",
            (nombre_plan,id_planes)
         )
         conexion.commit()
         return True
       except: 
         return False
    @staticmethod
    def actualizarPrecio(id_planes,precio_plan):
       try:
         cursor.execute(
            "update planes set precio_plan=%s where id_planes=%s",
            (precio_plan,id_planes)
         )
         conexion.commit()
         return True
       except: 
         return False
    
    
    @staticmethod
    def eliminar(id_planes):
        try:
          cursor.execute(
            "delete from clientes where id_planes=%s",
            (id_planes,)
          ) 
          conexion.commit() 
          return True  
        except:    
          return False
