#Hacer un programa que tenga una lista de 8 numeros enteros y realice lo siguiente: 
#a.- Recorrer la lista y mostrarla
#b.- hacer una funcion que recorra la lista de numeros y devuelva un string
#c.- ordenarla y mostrarla
#d.- mostrar su longitud
#e.- buscar algun elemento que el usuario pida por teclado


ListaN=[8,7,15,34,15,69,1,6]

#a
tamanio=len(ListaN)
i=0
while i >= len(ListaN)-1:
    print(ListaN[i])
    i+=1

#b
def lista_a_string(lista):
    return ' '.join(map(str, lista))

ListaN = [8, 7, 15, 34, 15, 69, 1, 6]
resultado = lista_a_string(ListaN)

print(resultado)

#c
print(ListaN)
ListaN.sort()
print(ListaN)

#d
def lista_a_string(lista):
    return ' '.join(map(str, lista))

ListaN = [8, 7, 15, 34, 15, 69, 1, 6]
longitud_lista = len(ListaN)
print(f"La longitud de la lista es: {longitud_lista}")
