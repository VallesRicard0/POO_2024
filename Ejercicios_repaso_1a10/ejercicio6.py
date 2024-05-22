# Función para imprimir una tabla de multiplicar
def imprimir_tabla(n):
    print(f"### Tabla del {n} ###")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
    print()  # Línea en blanco para separar las tablas

# Imprimir las tablas de multiplicar del 1 al 10
for num in range(1, 11):
    imprimir_tabla(num)