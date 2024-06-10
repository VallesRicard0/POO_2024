paises=("Mexico", "USA", "Brasil", "Japan")
numeros=(23,100,3.1416,100)
vario=["Hola", True, 100, 10.22]

#Ordenra lista
print(paises)
paises.sort()
print(paises)
print(numeros)
numeros.sort()


#como agregar elementos a la lista
print(numeros)
numeros.insert(len(numeros),100)
print(numeros)
numeros.append(100)


#Eliminar un numero
print(numeros)
numeros.pop(2)
print(numeros)
numeros.remove(100)

#Buscar en una lista un dato 
encontrar="Brasil"in paises
print(encontrar)

#Dar la vuelta a la lista
print(vario)
vario.reverse()
print(vario)


#Concatenar o unir listas
print(paises)
paises.extend(numeros)
print(paises)

#Vacia una lista
print(vario)
vario.clear()
print(vario)