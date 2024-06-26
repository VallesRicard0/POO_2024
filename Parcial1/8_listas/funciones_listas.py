
"list  (Array)"

#son colecciones o conjunto de datos/valores bajo un mismo nombre, para acceder a los valores se hace con un indice numerico
#Nota: sus valores si son modificables
#La lista en una coleccion ordenada y modificable permite miembros duplicados


#Crear una lista de numeros e imprimir el contenido

numeros=[23,34]
print(numeros)
#Ejemplo for
for i in numeros:
    print(i)
#Ejemplo while
tamanio=len(numeros)
i=0
while i >= len(numeros)-1:
    print(numeros[i])
    i+=1






#Crear una lista de palabras y que posteriormente busque una coincidencia de una palabra
palabras=["naranja","utd","america","azul"]
palabra_buscar=input("Ingrese la palabra a buscar")
if palabra_buscar in palabras:
    print(f"{palabra_buscar} está en la lista.")
else:
    print(f"{palabra_buscar} no está en la lista.")


#Ejemplo realizado en while
palabras = ["naranja", "utd", "america", "azul"]
palabra_buscar = input("Ingrese la palabra a buscar: ")

encontrada = False
i = 0
while i < len(palabras):
    if palabras[i] == palabra_buscar:
        encontrada = True
    i += 1

if encontrada:
    print(f"{palabra_buscar} está en la lista.")
else:
    print(f"{palabra_buscar} no está en la lista.")





#Ejemplo 3 agregar y eliminar elementos de una lista
#-os.system("clear")
numeros=[23,34,23]
print(numeros)

#Agregar un elemento
numeros.append(100)
print(numeros)
numeros.insert(3,200)
print(numeros)

#Eliminar un elemento
numeros.remove(100)#Indica el elemento a borrar
print(numeros)
numeros.pop(2)#Indica la posicion de elementos a borrar
print(numeros)


#Ejemolo 4 lista multi lineas para agregar los nombres y numeros telefonicos
agenda= [
["carlos",6183602434]
["Leo", 6183951475]
["Alberto", 6182225968]
["Pedro", 6186964878]
]
print(agenda)

for i in agenda:
    print(f"{agenda.index[i]+1},-{i}")



#Crea un programa que permita gestionar (actualizar) peliculas, colocar un menu de opciones para agregar , remover y consultar peliculas ademas de vaciar las peliculas
#Notas
#1 utilizar funciones y mandarlas a llamar desde otra carpeta
#2 utilizar listas para almacenar los nombres de las peliculas


