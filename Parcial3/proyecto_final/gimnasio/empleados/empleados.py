from conexionBD import *

class Empleado:
    def __init__(self, id_empleado, nombre, apellidos, puesto, salario, horario):
       self.id_empleado=id_empleado
       self.nombre=nombre
       self.apellidos=apellidos
       self.puesto=puesto
       self.salario=salario
       self.horario=horario
        

    def crear(self):
        try:
          cursor.execute(
            "insert into empleados values(null,%s,%s,%s,%s,%s);",
            (self.nombre,self.apellidos,self.puesto,self.salario,self.horario)
          )
          conexion.commit()
          return True
        except:
          return False
    @staticmethod
    def mostrar(id_empleado):
        try:
          cursor.execute(
            "select * from empleados where id_empleado=%s",
            (id_empleado,)
            
          )
          return cursor.fetchall()
        except:    
          return []

    @staticmethod
    def actualizar(id_empleado,nombre,apellidos,puesto,salario,horario):
       try:
         cursor.execute(
            "update empleados set nombre=%s, apellidos=%s, puesto=%s, salario=%s, horario=%s where id_clientes=%s",
            (nombre,apellidos,puesto,salario,horario,id_empleado)
         )
         conexion.commit()
         return True
       except: 
         return False
    
    @staticmethod
    def eliminar(id_empleado):
        try:
          cursor.execute(
            "delete from empleados where id_empleado=%s",
            (id_empleado,)
          ) 
          conexion.commit() 
          return True  
        except:    
          return False
    

