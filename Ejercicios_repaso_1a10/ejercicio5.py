# Solicitar dos números al usuario
numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))

# Verificar cuál número es mayor y cuál es menor
if numero1 > numero2:
    menor = numero2
    mayor = numero1
else:
    menor = numero1
    mayor = numero2

# Mostrar todos los números entre el menor y el mayor (excluyendo los extremos)
print(f"Números entre {menor} y {mayor}:")
for numero in range(menor + 1, mayor):
    print(numero)