#Ciclo For: Estructura iterativa que se ejecuta x veces

#Sintaxis
# for variable in elemento_iterable (lista, rango, etc)
#-------Bloque de instrucciones

#Ejemplo 1 Crear un programa que imprima en pantall 5 veces el @

contador = 1

for contador in range(1,6):
    print('@')

contador = 0

for contador in range(0,5):
    print('@')

#Ejemplo 2 crear un programa que imprima los numero del 1 al 5
#los sume y al final imprima la suma

res = 1
suma=0
for res in range (1,6):
    print (res)
    suma +=res
    print (suma)

# Ejemplo 3 crear un programa que imprima la tabla de multiplicar que el usuario desee

tabla = int(input("Ingresa un numero para calcular su tabla de multiplicar: "))

i=1
multi = 0

for i in range (1,11):
    multi = i * tabla
    print (f"{tabla} x {i} = {multi}")