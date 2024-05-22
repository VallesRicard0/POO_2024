#El ciclo while es una estructura iterativa que se ejecuta x veces siempre y cuando 
#la condicion se cumpla y se seguira ejecutando tantas veces como sea true la condicion

#Sintaxis
# while condicion
# bloque de instrucciones

#ejemplo 1 crear un programa que imprima en pantall 5 veces el @

#contador = 1

#while contador <=5:
    #print('@')
    #contador +=1



#Ejemplo 2 crear un programa que imprima los numero del 1 al 5
#los sume y al final imprima la suma
"""
res = 1
suma=0
while res <=5:
    print (res)
    suma +=res
    contador += 1

print ("la suma es: "(suma))
"""
# Ejemplo 3 crear un programa que imprima la tabla de multiplicar que el usuario desee

tabla = int(input("Ingresa un numero para calcular su tabla de multiplicar: "))

i=1
multi = 0

while i <=10:
    multi = i * tabla
    print (f"{tabla} x {i} = {multi}")
    i+=1
