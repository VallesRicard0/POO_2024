# Pedimos al usuario que introduzca los dos números
numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))

# Aseguramos que numero1 es menor que numero2, si no, los intercambiamos
if numero1 > numero2:
    numero1, numero2 = numero2, numero1

# Usamos un bucle for para iterar entre los dos números
print(f"Números impares entre {numero1} y {numero2}:")

for numero in range(numero1, numero2 + 1):
    if numero % 2 != 0:
        print(numero)
        