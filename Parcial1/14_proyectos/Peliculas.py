peliculas = []

def mostrar_menu():
    print("\nGestión de Películas")
    print("1. Agregar película")
    print("2. Remover película")
    print("3. Consultar películas")
    print("4. Actualizar película")
    print("5. Buscar película")
    print("6. Vaciar lista de películas")
    print("7. Salir")

def confirmar_accion():
    confirmacion = input("¿Está seguro de realizar esta acción? (si/no): ")
    return confirmacion.lower() == "si"

def agregar_pelicula():
    if confirmar_accion():
        titulo = input("Ingrese el título de la película: ")
        genero = input("Ingrese el género de la película: ")
        anio = input("Ingrese el año de la película: ")
        pelicula = {"titulo": titulo, "genero": genero, "año": anio}
        peliculas.append(pelicula)
        print("Película agregada exitosamente.")

def remover_pelicula():
    if confirmar_accion():
        titulo = input("Ingrese el título de la película que desea remover: ")
        for pelicula in peliculas:
            if pelicula["titulo"] == titulo:
                peliculas.remove(pelicula)
                print("Película removida exitosamente.")
                return
        print("Película no encontrada.")

def consultar_peliculas():
    if peliculas:
        for pelicula in peliculas:
            print(f"Título: {pelicula}")
    else:
        print("No hay películas en la lista.")

def actualizar_pelicula():
    if confirmar_accion():
        titulo = input("Ingrese el título de la película que desea actualizar: ")
        for pelicula in peliculas:
            if pelicula["titulo"] == titulo:
                genero = input("Ingrese el nuevo género de la película: ")
                anio = input("Ingrese el nuevo año de la película: ")
                pelicula["genero"] = genero
                pelicula["año"] = anio
                print("Película actualizada exitosamente.")
                return
        print("Película no encontrada.")

def buscar_pelicula():
    if confirmar_accion():
        titulo = input("Ingrese el título de la película que desea buscar: ")
        for pelicula in peliculas:
            if pelicula["titulo"] == titulo:
                print(f"Se encontró la película: {pelicula}")
                return
        print("Película no encontrada.")

def vaciar_peliculas():
    if confirmar_accion():
        peliculas.clear()
        print("Lista de películas vaciada exitosamente.")

opcion = ""
while opcion != "7":
    mostrar_menu()
    opcion = input("Seleccione una opción (1/2/3/4/5/6/7): ")

    if opcion == "1":
        agregar_pelicula()
    elif opcion == "2":
        remover_pelicula()
    elif opcion == "3":
        consultar_peliculas()
    elif opcion == "4":
        actualizar_pelicula()
    elif opcion == "5":
        buscar_pelicula()
    elif opcion == "6":
        vaciar_peliculas()
    elif opcion == "7":
        print("Saliendo del programa...")
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")