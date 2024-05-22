# Escribir un programa que muestre los cuadrados 
#(un numero multiplicado por si mismo) de los 60 primeros 
#numeros naturales. Resolverlo con while y for

multi=0
Contador=1
while Contador<=60:
    multi=Contador*Contador
    print(f"El cuadrado de {Contador} es {multi}")
    Contador=Contador+1
    
for contador in range(1,61):
    cuadrado=contador*contador
    
