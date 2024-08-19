from conexionBD import *

class Cliente:
    def __init__(self, id_clientes, nombre, apellidos, plan):
       self.id_clientes=id_clientes
       self.nombre=nombre
       self.apellidos=apellidos
       self.plan=plan
        

    def crear(self):
        try:
          cursor.execute(
            "insert into clientes values(null,%s,%s,%s);",
            (self.nombre,self.apellidos,self.plan)
          )
          conexion.commit()
          return True
        except:
          return False
    @staticmethod
    def mostrar(id_clientes):
        try:
          cursor.execute(
            "select * from clientes where id_clientes=%s",
            (id_clientes,)
            
          )
          return cursor.fetchall()
        except:    
          return []

    @staticmethod
    def actualizar(id_clientes,nombre,apellidos,plan):
       try:
         cursor.execute(
            "update clientes set nombre=%s, apellidos=%s, plan=%s where id_clientes=%s",
            (nombre,apellidos,plan,id_clientes)
         )
         conexion.commit()
         return True
       except: 
         return False
    
    @staticmethod
    def eliminar(id_clientes):
        try:
          cursor.execute(
            "delete from clientes where id_clientes=%s",
            (id_clientes,)
          ) 
          conexion.commit() 
          return True  
        except:    
          return False
    

