import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import StringVar, IntVar, Entry, Button, Label, Frame, Listbox

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
        return f"Hotel: {self.nombre}, ubicado en {self.ubicacion}"

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
        reservas_info = []
        for cliente in self.clientes:
            for reserva in cliente.reservas:
                reservas_info.append(f"Reserva {reserva.id_reserva} para el cliente {cliente.nombre}, desde {reserva.fecha_entrada} hasta {reserva.fecha_salida}, con el estado {reserva.estado}")
        return reservas_info

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Reservas")
        self.geometry("600x400")
        self.sistema_reserva = SistemaReserva()
        self.create_widgets()

    def create_widgets(self):
        self.menu = tk.Menu(self)
        self.config(menu=self.menu)
        
        self.menu.add_command(label="Clientes", command=self.menu_clientes)
        self.menu.add_command(label="Habitaciones", command=self.menu_habitaciones)
        self.menu.add_command(label="Hoteles", command=self.menu_hoteles)
        self.menu.add_command(label="Reservas", command=self.menu_reservas)
        self.menu.add_command(label="Salir", command=self.quit)

    def menu_clientes(self):
        self.new_window(ClientesWindow(self))

    def menu_habitaciones(self):
        self.new_window(HabitacionesWindow(self))

    def menu_hoteles(self):
        self.new_window(HotelesWindow(self))

    def menu_reservas(self):
        self.new_window(ReservasWindow(self))

    def new_window(self, window_class):
        window = window_class(self)
        self.wait_window(window)

class ClientesWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Menú de Clientes")
        self.geometry("400x300")
        self.parent = parent
        
        self.create_widgets()

    def create_widgets(self):
        tk.Button(self, text="Registrar Cliente", command=self.registrar_cliente).pack(pady=10)
        tk.Button(self, text="Eliminar Cliente", command=self.eliminar_cliente).pack(pady=10)
        tk.Button(self, text="Volver al Menú Principal", command=self.destroy).pack(pady=10)

    def registrar_cliente(self):
        id_cliente = simpledialog.askstring("ID Cliente", "Ingrese el ID del cliente:")
        nombre_cliente = simpledialog.askstring("Nombre Cliente", "Ingrese el nombre del cliente:")
        email_cliente = simpledialog.askstring("Email Cliente", "Ingrese el email del cliente:")
        if id_cliente and nombre_cliente and email_cliente:
            cliente = Cliente(id_cliente, nombre_cliente, email_cliente)
            self.parent.sistema_reserva.registrar_cliente(cliente)
            messagebox.showinfo("Éxito", f"Cliente {nombre_cliente} registrado exitosamente.")

    def eliminar_cliente(self):
        id_cliente = simpledialog.askstring("ID Cliente", "Ingrese el ID del cliente a eliminar:")
        cliente = next((c for c in self.parent.sistema_reserva.clientes if c.id_cliente == id_cliente), None)
        if cliente:
            self.parent.sistema_reserva.eliminar_cliente(cliente)
            messagebox.showinfo("Éxito", f"Cliente {cliente.nombre} eliminado exitosamente.")
        else:
            messagebox.showerror("Error", "Cliente no encontrado.")

class HabitacionesWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Menú de Habitaciones")
        self.geometry("400x300")
        self.parent = parent
        
        self.create_widgets()

    def create_widgets(self):
        tk.Button(self, text="Añadir Habitación", command=self.anadir_habitacion).pack(pady=10)
        tk.Button(self, text="Eliminar Habitación", command=self.eliminar_habitacion).pack(pady=10)
        tk.Button(self, text="Buscar Habitaciones", command=self.buscar_habitaciones).pack(pady=10)
        tk.Button(self, text="Volver al Menú Principal", command=self.destroy).pack(pady=10)

    def anadir_habitacion(self):
        nombre_hotel = simpledialog.askstring("Nombre Hotel", "Ingrese el nombre del hotel:")
        hotel = next((h for h in self.parent.sistema_reserva.hoteles if h.nombre == nombre_hotel), None)
        if hotel:
            numero = simpledialog.askstring("Número Habitación", "Ingrese el número de la habitación:")
            tipo = simpledialog.askstring("Tipo Habitación", "Ingrese el tipo de habitación:")
            precio = simpledialog.askfloat("Precio Habitación", "Ingrese el precio por noche:")
            if numero and tipo and precio is not None:
                habitacion = Habitacion(numero, tipo, precio)
                hotel.anadir_habitacion(habitacion)
                messagebox.showinfo("Éxito", f"Habitación {numero} añadida al hotel {nombre_hotel}.")
        else:
            messagebox.showerror("Error", "Hotel no encontrado.")

    def eliminar_habitacion(self):
        nombre_hotel = simpledialog.askstring("Nombre Hotel", "Ingrese el nombre del hotel:")
        hotel = next((h for h in self.parent.sistema_reserva.hoteles if h.nombre == nombre_hotel), None)
        if hotel:
            numero = simpledialog.askstring("Número Habitación", "Ingrese el número de la habitación a eliminar:")
            habitacion = next((hab for hab in hotel.habitaciones if hab.numero == numero), None)
            if habitacion:
                hotel.eliminar_habitacion(habitacion)
                messagebox.showinfo("Éxito", f"Habitación {numero} eliminada del hotel {nombre_hotel}.")
            else:
                messagebox.showerror("Error", "Habitación no encontrada.")
        else:
            messagebox.showerror("Error", "Hotel no encontrado.")

    def buscar_habitaciones(self):
        nombre_hotel = simpledialog.askstring("Nombre Hotel", "Ingrese el nombre del hotel:")
        hotel = next((h for h in self.parent.sistema_reserva.hoteles if h.nombre == nombre_hotel), None)
        if hotel:
            tipo = simpledialog.askstring("Tipo Habitación", "Ingrese el tipo de habitación (opcional):")
            precio_max = simpledialog.askfloat("Precio Máximo", "Ingrese el precio máximo (opcional):")
            resultados = hotel.buscar_habitacion(tipo, precio_max)
            result_window = tk.Toplevel(self)
            result_window.title("Resultados de Búsqueda")
            result_listbox = Listbox(result_window, width=50, height=10)
            result_listbox.pack(pady=10)
            for hab in resultados:
                result_listbox.insert(tk.END, hab.mostrar_info())
        else:
            messagebox.showerror("Error", "Hotel no encontrado.")

class HotelesWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Menú de Hoteles")
        self.geometry("400x300")
        self.parent = parent
        
        self.create_widgets()

    def create_widgets(self):
        tk.Button(self, text="Registrar Hotel", command=self.registrar_hotel).pack(pady=10)
        tk.Button(self, text="Eliminar Hotel", command=self.eliminar_hotel).pack(pady=10)
        tk.Button(self, text="Buscar Hoteles", command=self.buscar_hoteles).pack(pady=10)
        tk.Button(self, text="Mostrar Información del Hotel", command=self.mostrar_info_hotel).pack(pady=10)
        tk.Button(self, text="Volver al Menú Principal", command=self.destroy).pack(pady=10)

    def registrar_hotel(self):
        nombre_hotel = simpledialog.askstring("Nombre Hotel", "Ingrese el nombre del hotel:")
        ubicacion_hotel = simpledialog.askstring("Ubicación Hotel", "Ingrese la ubicación del hotel:")
        if nombre_hotel and ubicacion_hotel:
            hotel = Hotel(nombre_hotel, ubicacion_hotel)
            self.parent.sistema_reserva.registrar_hotel(hotel)
            messagebox.showinfo("Éxito", f"Hotel {nombre_hotel} registrado exitosamente.")

    def eliminar_hotel(self):
        nombre_hotel = simpledialog.askstring("Nombre Hotel", "Ingrese el nombre del hotel a eliminar:")
        hotel = next((h for h in self.parent.sistema_reserva.hoteles if h.nombre == nombre_hotel), None)
        if hotel:
            self.parent.sistema_reserva.eliminar_hotel(hotel)
            messagebox.showinfo("Éxito", f"Hotel {nombre_hotel} eliminado exitosamente.")
        else:
            messagebox.showerror("Error", "Hotel no encontrado.")

    def buscar_hoteles(self):
        ubicacion = simpledialog.askstring("Ubicación", "Ingrese la ubicación (opcional):")
        nombre = simpledialog.askstring("Nombre", "Ingrese el nombre (opcional):")
        resultados = self.parent.sistema_reserva.buscar_hoteles(ubicacion, nombre)
        result_window = tk.Toplevel(self)
        result_window.title("Resultados de Búsqueda")
        result_listbox = Listbox(result_window, width=50, height=10)
        result_listbox.pack(pady=10)
        for hotel in resultados:
            result_listbox.insert(tk.END, hotel.mostrar_info())

    def mostrar_info_hotel(self):
        nombre_hotel = simpledialog.askstring("Nombre Hotel", "Ingrese el nombre del hotel:")
        hotel = next((h for h in self.parent.sistema_reserva.hoteles if h.nombre == nombre_hotel), None)
        if hotel:
            messagebox.showinfo("Información del Hotel", hotel.mostrar_info())
        else:
            messagebox.showerror("Error", "Hotel no encontrado.")

class ReservasWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Menú de Reservas")
        self.geometry("400x300")
        self.parent = parent
        
        self.create_widgets()

    def create_widgets(self):
        tk.Button(self, text="Realizar Reserva", command=self.realizar_reserva).pack(pady=10)
        tk.Button(self, text="Cancelar Reserva", command=self.cancelar_reserva).pack(pady=10)
        tk.Button(self, text="Modificar Reserva", command=self.modificar_reserva).pack(pady=10)
        tk.Button(self, text="Listar Reservas", command=self.listar_reservas).pack(pady=10)
        tk.Button(self, text="Volver al Menú Principal", command=self.destroy).pack(pady=10)

    def realizar_reserva(self):
        id_cliente = simpledialog.askstring("ID Cliente", "Ingrese el ID del cliente:")
        cliente = next((c for c in self.parent.sistema_reserva.clientes if c.id_cliente == id_cliente), None)
        if cliente:
            nombre_hotel = simpledialog.askstring("Nombre Hotel", "Ingrese el nombre del hotel:")
            hotel = next((h for h in self.parent.sistema_reserva.hoteles if h.nombre == nombre_hotel), None)
            if hotel:
                numero_hab = simpledialog.askstring("Número Habitación", "Ingrese el número de la habitación:")
                habitacion = next((hab for hab in hotel.habitaciones if hab.numero == numero_hab), None)
                if habitacion and habitacion.disponible:
                    fecha_entrada = simpledialog.askstring("Fecha Entrada", "Ingrese la fecha de entrada (YYYY-MM-DD):")
                    fecha_salida = simpledialog.askstring("Fecha Salida", "Ingrese la fecha de salida (YYYY-MM-DD):")
                    id_reserva = simpledialog.askstring("ID Reserva", "Ingrese el ID de la reserva:")
                    reserva = Reserva(id_reserva, habitacion, cliente, fecha_entrada, fecha_salida)
                    cliente.realizar_reserva(reserva)
                    habitacion.actualizar_disponibilidad(False)
                    messagebox.showinfo("Éxito", f"Reserva {id_reserva} realizada con éxito.")
                else:
                    messagebox.showerror("Error", "Habitación no disponible o no encontrada.")
            else:
                messagebox.showerror("Error", "Hotel no encontrado.")
        else:
            messagebox.showerror("Error", "Cliente no encontrado.")

    def cancelar_reserva(self):
        id_cliente = simpledialog.askstring("ID Cliente", "Ingrese el ID del cliente:")
        cliente = next((c for c in self.parent.sistema_reserva.clientes if c.id_cliente == id_cliente), None)
        if cliente:
            id_reserva = simpledialog.askstring("ID Reserva", "Ingrese el ID de la reserva a cancelar:")
            reserva = next((r for r in cliente.reservas if r.id_reserva == id_reserva), None)
            if reserva:
                cliente.cancelar_reserva(reserva)
                reserva.habitacion.actualizar_disponibilidad(True)
                messagebox.showinfo("Éxito", f"Reserva {id_reserva} cancelada.")
            else:
                messagebox.showerror("Error", "Reserva no encontrada.")
        else:
            messagebox.showerror("Error", "Cliente no encontrado.")

    def modificar_reserva(self):
        id_cliente = simpledialog.askstring("ID Cliente", "Ingrese el ID del cliente:")
        cliente = next((c for c in self.parent.sistema_reserva.clientes if c.id_cliente == id_cliente), None)
        if cliente:
            id_reserva = simpledialog.askstring("ID Reserva", "Ingrese el ID de la reserva a modificar:")
            reserva = next((r for r in cliente.reservas if r.id_reserva == id_reserva), None)
            if reserva:
                nueva_fecha_entrada = simpledialog.askstring("Nueva Fecha Entrada", "Ingrese la nueva fecha de entrada (YYYY-MM-DD):")
                nueva_fecha_salida = simpledialog.askstring("Nueva Fecha Salida", "Ingrese la nueva fecha de salida (YYYY-MM-DD):")
                reserva.modificar_reserva(nueva_fecha_entrada, nueva_fecha_salida)
                messagebox.showinfo("Éxito", f"Reserva {id_reserva} modificada.")
            else:
                messagebox.showerror("Error", "Reserva no encontrada.")
        else:
            messagebox.showerror("Error", "Cliente no encontrado.")

    def listar_reservas(self):
        reservas_info = self.parent.sistema_reserva.listar_reservas()
        result_window = tk.Toplevel(self)
        result_window.title("Listado de Reservas")
        result_listbox = Listbox(result_window, width=80, height=20)
        result_listbox.pack(pady=10)
        for info in reservas_info:
            result_listbox.insert(tk.END, info)

if __name__ == "__main__":
    app = App()
    app.mainloop()
