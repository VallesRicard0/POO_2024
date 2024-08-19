from Autos import Clase
from funciones import *
from CRUD import *
def menu_principal():
    while True:    
        borrarPantalla()
        print("""
      .::  Menu Principal ::. 
          1.- Insertar nuevo registro
          2.- Consultar registro
          3.- Actualizar registro
          4.- Eliminar registro
          """)
        opcion = input("\t Elige una opción: ").upper()
       
        if opcion == '1' or opcion=="INSERTAR REGISTRO":
            borrarPantalla()
            print("\n \t ..:: Registro en el Sistema ::..")
            Matricula=input("\t ¿Cual es tu matricula?: ")
            Marca=input("\t ¿Cuales es tu marca?: ")
            Modelo=input("\t ingresa el modelo: ")
            color= input("Ingrese el color")
            nif= input("Ingrese su nif")
            Clase.insertar(Matricula, Marca, Modelo, color, nif)
            print("\n \t Registro exitoso")
            input("\n \t Presiona Enter para continuar")
            menu_principal()
        elif opcion == '2' or opcion=="CONSULTAR REGISTRO":
            borrarPantalla()
            print("\n \t ..:: Consultar Registro ::..")
            Matricula=input("\t ¿Cual es tu matricula?: ")
            resultado = Clase.consultar(Matricula)
            print("\n \t Registro encontrado")
            print("\n \t Matricula: ", resultado[0][0])
            print("\n \t Marca: ", resultado[0][1])
            print("\n \t Modelo: ", resultado[0][2])
            print("\n \t Color: ", resultado[0][3])
            print("\n \t NIF: ", resultado[0][4])
            input("\n \t Presiona Enter para continuar")
            menu_principal()
        elif opcion == '3' or opcion=="ACTUALIZAR REGISTRO":
             borrarPantalla()
             print("\n \t ..:: Actualizar Registro ::..")
             Matricula=input("\t ¿Cual es tu matricula?: ")
             Marca=input("\t ¿Cuales es tu marca?: ")
             Modelo=input("\t ingresa el modelo: ")
             
