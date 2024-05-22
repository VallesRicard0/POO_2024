"""

Existe una estructura de condicion llamada "if"
la cual evalua una condicion para encrontrar el valor "true" y su se cumple
la condicion se ejecuta la o las lineas de codigo

Tienes 4 variables de if

1.-If simple
2.-If compuesto
3.-If anidado
3.-Elif

"""
"""
#Ejemplo 1 If simple
color=input("Ingresa un color: ")

if color == "rojo":
    print("Soy el color rojo ")

#Ejemplo 2 If compuesto
color=input("Ingresa un color: ")

if color == "rojo":
    print("Soy el color rojo ")
else:
    print ("No soy el color rojo soy otra cosa")

#Ejemplo 3 If anidado
color=input("Ingresa un color: ")

if color == "rojo":
    print("Soy el color rojo ")
    if color !=  "rojo":
        print("no soy el color rojo")
else:
    print ("No soy el color orjo soy otra cosa")

#Ejemplo 4 If Elif
color=input("Ingresa un color: ")

if color == "rojo":
    print("Soy el color rojo ")
elif color== "amarillo":
     print("Soy el color amarillo ")
elif color== "azul":
     print("Soy el color azul ")
elif color== "morado":
     print("Soy el color morado ")
else:
    print("No soy ningun color de los anteriores")
"""
#Ejemplo 5 crear un programa que solicite el numero de la semana 
# e imprima en pantalla el dia que le corresponde

dia=input ("Ingresa un numero del 1 al 7: ")
if dia == "1":
    print ("Lunes")
elif dia == "2":
     print("Martes ")
elif dia == "3":
     print("Miercoles")
elif dia == "4":
     print("Jueves")
elif dia == "5":
     print("Viernes ")
elif dia == "6":
     print("Sabado")
elif dia == "7":
     print("Domingo")
else:
    print("No soy ningun dia de la semana")