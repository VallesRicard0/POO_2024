"""
Comentario de variass lineas
Nota: A la hora de concatenar no es posible incluir en 
algunas ocasiones conetindo de variables que no sean del tipo str

"""
#Comentario de una linea

#Concatenar un str con str

texto= "Soy una cadena"
numero = 23

print (texto+" y soy otra cadena")

#Concatenar un int con str

numero = 23
numero_str=str(numero)

print ("El numero es: "+numero_str)

print ("El numero es: "+str(numero))

#Concatenar un str con int

n1 = '23'
n2 = 33

suma = int(n1) + n2

print("El número es: " + str(suma))

#Concatenar un float y int con str

n1='23'
n2=33.1

suma= int(n1)+n2

print ("El numero es: "+str(int(suma)))
print(f"El numero: {int(suma)}")

#Concatenar un float y float con float

n1='23.34'
n2='33.99'

suma=float(n1)+float(n2)
print(f"El numero: {int(suma)}")


