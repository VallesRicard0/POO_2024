#Una funcion es  un conjunto de intrucciones agrupadas bajo un nombre en particular


#Sintaxis
#def nombreDeMifuncion(parametros):
    
#bloque o conjunto de instrucciones
#las funciones pueden ser de 4 tipos 
#1_ Funcion que no recibe parametros y no representa valor
#2_ Funcion que no recibe parametros y regresa valor
#3_ Funcion que recibe parametros y no regresa valor
#4_ Funcion que recibe parametros y regresa valor

#Crear una funcion que regrese nombres de personas
#1_ Funcion que no recibe parametros y no representa valor
def solicitarNombre():
    nombre=input("Ingrese el nombre de una persona")
solicitarNombre()

#Ejemplo 2
def suma():
    n1=int(input("Numero #1:"))
    n2=int(input("Numero #2: "))
    suma=n1+n2
    print(f"{n1}+{n2}={suma}")
suma()

#Ejemplo 3
#2_ Funcion que no recibe parametros y regresa valor
def suma():
    n1=int(input("Numero #1:"))
    n2=int(input("Numero #2: "))
    suma=n1+n2
    return suma
resultado_suma=suma()
print(f"la suma es: (resultado_suma)")

#Ejemplo 4
#3_ Funcion que recibe parametros y no regresa valor
def suma(n1,n2):

    suma=n1+n2
    print(f"la suma es: {suma}")

n1=int(input("Numero #1:"))
n2=int(input("Numero #2: "))
suma(n1,n2)

#Elemplo 5
#4_ Funcion que recibe parametros y regresa valor
def suma(n1,n2):
    suma=n1+n2
    return suma

n1=int(input("Numero #1:"))
n2=int(input("Numero #2: "))
resultado_suma=suma(n1,n2)
print(f"La suma es: {resultado_suma}")



#Ejemplo 6
#Crar un programa que solicite a travez de una funcion lo siguiente informacion: nombre del paciente, Edad, Estatura, Tipo de sangre. Utiliza las 4  tipos de funciones

