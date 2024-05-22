while True:
    # Pedimos al usuario que introduzca un número
    numero = int(input("Introduce un número (111 para salir): "))
    
    # Verificamos si el número es 111
    if numero == 111:
        print("Se ha introducido 111. Terminando el programa...")
        break  # Salimos del bucle y terminamos el programa
    else:
        # Mostramos el número introducido
        print(f"Has introducido el número: {numero}")