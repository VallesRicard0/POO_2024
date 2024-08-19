import Cliente
import Habitacion
import Hotel
import Reservacion
import Sistema_Reserva



def mostrar_menu():
    print("=== Menú del Sistema de Reservas ===\n")
    
    print("1. Clientes")
    print("2. Habitaciones")
    print("3. Hoteles")
    print("4. Reservas")
    print("5. Salir")

def menu_clientes(sistema_reserva):
    while True:
        print("\n=== Menú de Clientes ===")
        print("1. Registrar cliente")
        print("2. Eliminar cliente")
        print("3. Volver al menú principal")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            id_cliente = input("Ingrese el ID del cliente: ")
            nombre_cliente = input("Ingrese el nombre del cliente: ")
            email_cliente = input("Ingrese el email del cliente: ")
            cliente = Cliente(id_cliente, nombre_cliente, email_cliente)
            sistema_reserva.registrar_cliente(cliente)
        
        elif opcion == "2":
            id_cliente = input("Ingrese el ID del cliente a eliminar: ")
            cliente = next((c for c in sistema_reserva.clientes if c.id_cliente == id_cliente), None)
            if cliente:
                sistema_reserva.eliminar_cliente(cliente)
            else:
                print("Cliente no encontrado.")
        
        elif opcion == "3":
            break

def menu_habitaciones(sistema_reserva):
    while True:
        print("\n=== Menú de Habitaciones ===")
        print("1. Añadir habitación a un hotel")
        print("2. Eliminar habitación de un hotel")
        print("3. Buscar habitaciones en un hotel")
        print("4. Volver al menú principal")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nombre_hotel = input("Ingrese el nombre del hotel: ")
            hotel = next((h for h in sistema_reserva.hoteles if h.nombre == nombre_hotel), None)
            if hotel:
                numero = input("Ingrese el número de la habitación: ")
                tipo = input("Ingrese el tipo de habitación: ")
                precio = float(input("Ingrese el precio por noche: "))
                habitacion = Habitacion(numero, tipo, precio)
                hotel.anadir_habitacion(habitacion)
            else:
                print("Hotel no encontrado.")
        
        elif opcion == "2":
            nombre_hotel = input("Ingrese el nombre del hotel: ")
            hotel = next((h for h in sistema_reserva.hoteles if h.nombre == nombre_hotel), None)
            if hotel:
                numero = input("Ingrese el número de la habitación a eliminar: ")
                habitacion = next((hab for hab in hotel.habitaciones if hab.numero == numero), None)
                if habitacion:
                    hotel.eliminar_habitacion(habitacion)
                else:
                    print("Habitación no encontrada.")
            else:
                print("Hotel no encontrado.")
        
        elif opcion == "3":
            nombre_hotel = input("Ingrese el nombre del hotel: ")
            hotel = next((h for h in sistema_reserva.hoteles if h.nombre == nombre_hotel), None)
            if hotel:
                tipo = input("Ingrese el tipo de habitación (opcional): ")
                precio_max = input("Ingrese el precio máximo (opcional): ")
                precio_max = float(precio_max) if precio_max else None
                resultados = hotel.buscar_habitacion(tipo, precio_max)
                for hab in resultados:
                    print(hab.mostrar_info())
            else:
                print("Hotel no encontrado.")
        
        elif opcion == "4":
            break

def menu_hoteles(sistema_reserva):
    while True:
        print("\n=== Menú de Hoteles ===")
        print("1. Registrar hotel")
        print("2. Eliminar hotel")
        print("3. Buscar hoteles")
        print("4. Mostrar información de un hotel")
        print("5. Volver al menú principal")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nombre_hotel = input("Ingrese el nombre del hotel: ")
            ubicacion_hotel = input("Ingrese la ubicación del hotel: ")
            hotel = Hotel(nombre_hotel, ubicacion_hotel)
            sistema_reserva.registrar_hotel(hotel)
        
        elif opcion == "2":
            nombre_hotel = input("Ingrese el nombre del hotel a eliminar: ")
            hotel = next((h for h in sistema_reserva.hoteles if h.nombre == nombre_hotel), None)
            if hotel:
                sistema_reserva.eliminar_hotel(hotel)
            else:
                print("Hotel no encontrado.")
        
        elif opcion == "3":
            ubicacion = input("Ingrese la ubicación (opcional): ")
            nombre = input("Ingrese el nombre (opcional): ")
            resultados = sistema_reserva.buscar_hoteles(ubicacion, nombre)
            for hotel in resultados:
                hotel.mostrar_info()
        
        elif opcion == "4":
            nombre_hotel = input("Ingrese el nombre del hotel: ")
            hotel = next((h for h in sistema_reserva.hoteles if h.nombre == nombre_hotel), None)
            if hotel:
                hotel.mostrar_info()
            else:
                print("Hotel no encontrado.")
        
        elif opcion == "5":
            break

def menu_reservas(sistema_reserva):
    while True:
        print("\n=== Menú de Reservas ===")
        print("1. Realizar reserva")
        print("2. Cancelar reserva")
        print("3. Modificar reserva")
        print("4. Listar reservas de todos los clientes")
        print("5. Volver al menú principal")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            id_cliente = input("Ingrese el ID del cliente: ")
            cliente = next((c for c in sistema_reserva.clientes if c.id_cliente == id_cliente), None)
            if cliente:
                nombre_hotel = input("Ingrese el nombre del hotel: ")
                hotel = next((h for h in sistema_reserva.hoteles if h.nombre == nombre_hotel), None)
                if hotel:
                    numero_hab = input("Ingrese el número de la habitación: ")
                    habitacion = next((hab for hab in hotel.habitaciones if hab.numero == numero_hab), None)
                    if habitacion and habitacion.disponible:
                        fecha_entrada = input("Ingrese la fecha de entrada (YYYY-MM-DD): ")
                        fecha_salida = input("Ingrese la fecha de salida (YYYY-MM-DD): ")
                        id_reserva = input("Ingrese el ID de la reserva: ")
                        reserva =(id_reserva, habitacion, cliente, fecha_entrada, fecha_salida)
                        cliente.realizar_reserva(reserva)
                        habitacion.actualizar_disponibilidad(False)
                    else:
                        print("Habitación no disponible o no encontrada.")
                else:
                    print("Hotel no encontrado.")
            else:
                print("Cliente no encontrado.")
        
        elif opcion == "2":
            id_cliente = input("Ingrese el ID del cliente: ")
            cliente = next((c for c in sistema_reserva.clientes if c.id_cliente == id_cliente), None)
            if cliente:
                id_reserva = input("Ingrese el ID de la reserva a cancelar: ")
                reserva = next((r for r in cliente.reservas if r.id_reserva == id_reserva), None)
                if reserva:
                    cliente.cancelar_reserva(reserva)
                    reserva.habitacion.actualizar_disponibilidad(True)
                else:
                    print("Reserva no encontrada.")
            else:
                print("Cliente no encontrado.")
        
        elif opcion == "3":
            id_cliente = input("Ingrese el ID del cliente: ")
            cliente = next((c for c in sistema_reserva.clientes if c.id_cliente == id_cliente), None)
            if cliente:
                id_reserva = input("Ingrese el ID de la reserva a modificar: ")
                reserva = next((r for r in cliente.reservas if r.id_reserva == id_reserva), None)
                if reserva:
                    nueva_fecha_entrada = input("Ingrese la nueva fecha de entrada (YYYY-MM-DD): ")
                    nueva_fecha_salida = input("Ingrese la nueva fecha de salida (YYYY-MM-DD): ")
                    reserva.modificar_reserva(nueva_fecha_entrada, nueva_fecha_salida)
                else:
                    print("Reserva no encontrada.")
            else:
                print("Cliente no encontrado.")
        
        elif opcion == "4":
            sistema_reserva.listar_reservas()
        
        elif opcion == "5":
            break

def main():
    sistema_reserva = SistemaReserva()
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            menu_clientes(sistema_reserva)
        
        elif opcion == "2":
            menu_habitaciones(sistema_reserva)
        
        elif opcion == "3":
            menu_hoteles(sistema_reserva)
        
        elif opcion == "4":
            menu_reservas(sistema_reserva)
        
        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
