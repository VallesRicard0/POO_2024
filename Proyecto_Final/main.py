
import mysql.connector
import os

# Lee la contraseña desde una variable de entorno
password = os.environ.get('MYSQL_PASSWORD')

try:
    # Conectar con la BD en MySQL
    conexion = mysql.connector.connect(
        host='localhost',
        user='root',
        password=password,
        database='hotel23'
    )
    # Crear un objeto de tipo cursor que se pueda reutilizar nuevamente
    cursor = conexion.cursor(buffered=True)
except mysql.connector.Error as err:
    print(f"Error al conectar a la base de datos: {err}")
finally:
    # Cierra la conexión
    if conexion:
        conexion.close()

class Cliente:
    def __init__(self, id_cliente, nombre, email):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.email = email
        self.reservas = []

    def realizar_reserva(self, reserva):
        self.reservas.append(reserva)
        reserva.estado = "Confirmada"
        print(f"Reserva {reserva.id_reserva} realizada con éxito para {self.nombre}, para la habitación {reserva.habitacion.numero}")

    def cancelar_reserva(self, reserva):
        if reserva in self.reservas:
            reserva.cancelar_reserva()
            self.reservas.remove(reserva)

class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.precio = precio
        self.numero = numero
        self.tipo = tipo
        self.disponible = True  # Se añade el atributo disponible
    
    def actualizar_disponibilidad(self, disponible):
        self.disponible = disponible
        estado = "Disponible" if disponible else "No disponible"
        print(f"La habitación {self.numero} está {estado}")
    
    def mostrar_info(self):
        return f"Habitación {self.numero}, Tipo: {self.tipo}, Precio: {self.precio} por noche"

class Hotel:
    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.habitaciones = []
    
    def anadir_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)
        print(f"Habitación {habitacion.numero} añadida al hotel {self.nombre}.")

    def eliminar_habitacion(self, habitacion):
        self.habitaciones.remove(habitacion)
        print(f"Habitación {habitacion.numero} eliminada del hotel {self.nombre}.")
    
    def buscar_habitacion(self, tipo=None, precio_max=None):
        resultados = []
        for habitacion in self.habitaciones:
            if (tipo is None or habitacion.tipo == tipo) and (precio_max is None or habitacion.precio <= precio_max):
                resultados.append(habitacion)
        return resultados
    
    def mostrar_info(self):
        print(f"Hotel: {self.nombre}, ubicado en {self.ubicacion}")

class Reserva:
    def __init__(self, id_reserva, habitacion, cliente, fecha_entrada, fecha_salida):
        self.id_reserva = id_reserva
        self.habitacion = habitacion
        self.cliente = cliente
        self.fecha_salida = fecha_salida
        self.fecha_entrada = fecha_entrada
        self.estado = "Pendiente"
    
    def modificar_reserva(self, nueva_fecha_entrada, nueva_fecha_salida):
        self.fecha_entrada = nueva_fecha_entrada
        self.fecha_salida = nueva_fecha_salida
        print(f"Reserva {self.id_reserva} modificada para las fechas {self.fecha_entrada} a {self.fecha_salida}")
    
    def cancelar_reserva(self):
        self.estado = "Cancelada"
        print(f"Reserva {self.id_reserva} se canceló")

class SistemaReserva:
    def __init__(self):
        self.hoteles = []
        self.clientes = []
    
    def registrar_hotel(self, hotel):
        self.hoteles.append(hotel)
        print(f"El hotel {hotel.nombre} fue registrado exitosamente.")
    
    def eliminar_hotel(self, hotel):
        self.hoteles.remove(hotel)
        print(f"El hotel {hotel.nombre} fue eliminado exitosamente.")

    def registrar_cliente(self, cliente):
        self.clientes.append(cliente)
        print(f"El cliente {cliente.nombre} fue registrado exitosamente.")

    def eliminar_cliente(self, cliente):
        self.clientes.remove(cliente)
        print(f"El cliente {cliente.nombre} fue eliminado exitosamente.")
    
    def buscar_hoteles(self, ubicacion=None, nombre=None):
        resultados = []
        for hotel in self.hoteles:
            if (ubicacion is None or hotel.ubicacion == ubicacion) and (nombre is None or hotel.nombre == nombre):
                resultados.append(hotel)
        return resultados
    
    def listar_reservas(self):
        for cliente in self.clientes:
            for reserva in cliente.reservas:
                print(f"Reserva {reserva.id_reserva} para el cliente {cliente.nombre}, desde {reserva.fecha_entrada} hasta {reserva.fecha_salida}, con el estado {reserva.estado}")

import os

def borrarPantalla():
    os.system("clear")  # Usa "cls" en Windows si es necesario

def esperarTecla():
    print("\n \t \tOprima cualquier tecla para continuar ...")
    input()

def mostrar_menu():
    borrarPantalla()
    print("=== Menú del Sistema de Reservas ===\n")
    print("1. Clientes")
    print("2. Habitaciones")
    print("3. Hoteles")
    print("4. Reservas")
    print("5. Salir")
    esperarTecla()

def menu_clientes(sistema_reserva):
    while True:
        borrarPantalla()
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
            esperarTecla()
        
        elif opcion == "2":
            id_cliente = input("Ingrese el ID del cliente a eliminar: ")
            cliente = next((c for c in sistema_reserva.clientes if c.id_cliente == id_cliente), None)
            if cliente:
                sistema_reserva.eliminar_cliente(cliente)
            else:
                print("Cliente no encontrado.")
            esperarTecla()
        
        elif opcion == "3":
            break

def menu_habitaciones(sistema_reserva):
    while True:
        borrarPantalla()
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
            esperarTecla()
        
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
            esperarTecla()
        
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
            esperarTecla()
        
        elif opcion == "4":
            break

def menu_hoteles(sistema_reserva):
    while True:
        borrarPantalla()
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
            esperarTecla()
        
        elif opcion == "2":
            nombre_hotel = input("Ingrese el nombre del hotel a eliminar: ")
            hotel = next((h for h in sistema_reserva.hoteles if h.nombre == nombre_hotel), None)
            if hotel:
                sistema_reserva.eliminar_hotel(hotel)
            else:
                print("Hotel no encontrado.")
            esperarTecla()
        
        elif opcion == "3":
            ubicacion = input("Ingrese la ubicación (opcional): ")
            nombre = input("Ingrese el nombre (opcional): ")
            resultados = sistema_reserva.buscar_hoteles(ubicacion, nombre)
            for hotel in resultados:
                hotel.mostrar_info()
            esperarTecla()
        
        elif opcion == "4":
            nombre_hotel = input("Ingrese el nombre del hotel: ")
            hotel = next((h for h in sistema_reserva.hoteles if h.nombre == nombre_hotel), None)
            if hotel:
                hotel.mostrar_info()
            else:
                print("Hotel no encontrado.")
            esperarTecla()
        
        elif opcion == "5":
            break

def menu_reservas(sistema_reserva):
    while True:
        borrarPantalla()
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
                        reserva = Reserva(id_reserva, habitacion, cliente, fecha_entrada, fecha_salida)
                        cliente.realizar_reserva(reserva)
                        habitacion.actualizar_disponibilidad(False)
                    else:
                        print("Habitación no disponible o no encontrada.")
                else:
                    print("Hotel no encontrado.")
            else:
                print("Cliente no encontrado.")
            esperarTecla()
        
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
            esperarTecla()
        
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
            esperarTecla()
        
        elif opcion == "4":
            sistema_reserva.listar_reservas()
            esperarTecla()
        
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
            esperarTecla()

if __name__ == "__main__":
    main()

