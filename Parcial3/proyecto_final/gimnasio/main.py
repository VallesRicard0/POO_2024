import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import StringVar, IntVar, Entry, Button, Label, Frame
import getpass

# Funciones de los módulos
from clientes import cliente
from planes import plan
from empleados import empleados
from usuarios import usuario
from servicios import servicio

def crear_ventana(title):
    ventana = tk.Tk()
    ventana.title(title)
    return ventana

def cerrar_ventana(ventana):
    ventana.destroy()

class App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x300")
        self.root.title("Sistema de Gestión")

        self.main_menu()

    def main_menu(self):
        self.clear_window()

        tk.Label(self.root, text="..::  Inicio de sesión ::..").pack()
        tk.Button(self.root, text="Registro", command=self.registro).pack(pady=10)
        tk.Button(self.root, text="Login", command=self.login).pack(pady=10)
        tk.Button(self.root, text="Salir", command=self.root.quit).pack(pady=10)

    def registro(self):
        self.clear_window()

        tk.Label(self.root, text="..:: Registro en el Sistema ::..").pack()

        self.nombre_entry = Entry(self.root)
        self.nombre_entry.pack(pady=5)
        self.nombre_entry.insert(0, "Nombre")

        self.apellidos_entry = Entry(self.root)
        self.apellidos_entry.pack(pady=5)
        self.apellidos_entry.insert(0, "Apellidos")

        self.email_entry = Entry(self.root)
        self.email_entry.pack(pady=5)
        self.email_entry.insert(0, "Email")

        self.password_entry = Entry(self.root, show="*")
        self.password_entry.pack(pady=5)
        self.password_entry.insert(0, "Contraseña")

        tk.Button(self.root, text="Registrar", command=self.registrar_usuario).pack(pady=10)
        tk.Button(self.root, text="Volver", command=self.main_menu).pack(pady=10)

    def registrar_usuario(self):
        nombre = self.nombre_entry.get()
        apellidos = self.apellidos_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()

        # Agregar lógica de registro aquí
        obj_usuario = usuario.Usuario(nombre, apellidos, email, password)
        resultado = obj_usuario.registrar()
        if resultado:
            messagebox.showinfo("Registro", f"{nombre} {apellidos}, se registró correctamente con el email: {email}")
        else:
            messagebox.showerror("Error", "No fue posible insertar el registro. Inténtelo de nuevo.")

    def login(self):
        self.clear_window()

        tk.Label(self.root, text="..:: Inicio de Sesión ::..").pack()

        self.email_entry = Entry(self.root)
        self.email_entry.pack(pady=5)
        self.email_entry.insert(0, "Email")

        self.password_entry = Entry(self.root, show="*")
        self.password_entry.pack(pady=5)
        self.password_entry.insert(0, "Contraseña")

        tk.Button(self.root, text="Login", command=self.iniciar_sesion).pack(pady=10)
        tk.Button(self.root, text="Volver", command=self.main_menu).pack(pady=10)

    def iniciar_sesion(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        # Agregar lógica de login aquí
        registro = usuario.Usuario.iniciar_sesion(email, password)
        if registro:
            self.menu_inicial()
        else:
            messagebox.showerror("Error", "Email y/o contraseña incorrectas. Vuelva a intentarlo.")

    def menu_inicial(self):
        self.clear_window()

        tk.Label(self.root, text="..:: Menu Principal ::..").pack()
        tk.Button(self.root, text="Cliente", command=self.menu_clientes).pack(pady=10)
        tk.Button(self.root, text="Empleado", command=self.menu_empleado).pack(pady=10)
        tk.Button(self.root, text="Salir", command=self.root.quit).pack(pady=10)

    def menu_clientes(self):
        self.clear_window()

        tk.Label(self.root, text="..:: Menu de Clientes ::..").pack()
        tk.Button(self.root, text="Mostrar Datos", command=self.mostrar_datos_cliente).pack(pady=5)
        tk.Button(self.root, text="Actualizar Datos", command=self.actualizar_datos_cliente).pack(pady=5)
        tk.Button(self.root, text="Darse de Baja", command=self.darse_de_baja).pack(pady=5)
        tk.Button(self.root, text="Volver", command=self.menu_inicial).pack(pady=10)

    def mostrar_datos_cliente(self):
        id_cliente = simpledialog.askstring("ID Cliente", "Coloca tu ID proporcionado por el empleado:")

        # Agregar lógica para mostrar datos del cliente aquí
        registros = cliente.Cliente.mostrar(id_cliente)
        if registros:
            info = "\n".join(f"Id: {fila[0]} - Nombre: {fila[1]} - Apellidos: {fila[2]} - Numero de plan: {fila[3]}" for fila in registros)
            messagebox.showinfo("Datos del Cliente", info)
        else:
            messagebox.showwarning("No Encontrado", "No existen clientes con ese ID.")

    def actualizar_datos_cliente(self):
        id_cliente = simpledialog.askstring("ID Cliente", "Id del cliente a actualizar:")
        nombre = simpledialog.askstring("Nombre", "Nombre:")
        apellidos = simpledialog.askstring("Apellidos", "Apellidos:")
        plan = simpledialog.askstring("Plan", "Plan a elegir:")

        # Agregar lógica para actualizar datos del cliente aquí
        resultado = cliente.Cliente.actualizar(id_cliente, nombre, apellidos, plan)
        if resultado:
            messagebox.showinfo("Actualización", "Cliente actualizado correctamente.")
        else:
            messagebox.showerror("Error", "No fue posible actualizar al cliente. Vuelva a intentarlo.")

    def darse_de_baja(self):
        id_cliente = simpledialog.askstring("ID Cliente", "Id del cliente a eliminar:")

        # Agregar lógica para eliminar al cliente aquí
        resultado = cliente.Cliente.eliminar(id_cliente)
        if resultado:
            messagebox.showinfo("Eliminación", "Cliente eliminado con éxito.")
        else:
            messagebox.showerror("Error", "No se pudo eliminar al cliente. Asegúrate de que el ID sea correcto.")

    def menu_empleado(self):
        self.clear_window()

        tk.Label(self.root, text="..:: Menu Empleados ::..").pack()
        tk.Button(self.root, text="Modificar Planes", command=self.modificar_planes).pack(pady=5)
        tk.Button(self.root, text="Modificar Clientes", command=self.modificar_clientes).pack(pady=5)
        tk.Button(self.root, text="Acceder Servicios", command=self.acceder_servicios).pack(pady=5)
        tk.Button(self.root, text="Modificar Empleados", command=self.modificar_empleados).pack(pady=5)
        tk.Button(self.root, text="Volver", command=self.menu_inicial).pack(pady=10)

    def modificar_planes(self):
        self.clear_window()

        tk.Label(self.root, text="..:: Menú de Planes ::..").pack()
        tk.Button(self.root, text="Modificar Precio", command=self.modificar_precio).pack(pady=5)
        tk.Button(self.root, text="Modificar Nombre", command=self.modificar_nombre).pack(pady=5)
        tk.Button(self.root, text="Añadir Plan", command=self.añadir_plan).pack(pady=5)
        tk.Button(self.root, text="Mostrar Planes", command=self.mostrar_planes).pack(pady=5)
        tk.Button(self.root, text="Volver", command=self.menu_empleado).pack(pady=10)

    def modificar_precio(self):
        id_plan = simpledialog.askstring("ID Plan", "Coloca el ID del plan a modificar:")
        precio_plan = simpledialog.askstring("Nuevo Precio", "Coloca el nuevo precio:")
        
        # Agregar lógica para modificar el precio del plan aquí
        resultado = plan.Plan.actualizarPrecio(id_plan, precio_plan)
        if resultado:
            messagebox.showinfo("Actualización", "Precio actualizado correctamente.")
        else:
            messagebox.showerror("Error", "Hubo un error al actualizar el precio. Vuelve a intentarlo.")

    def modificar_nombre(self):
        id_plan = simpledialog.askstring("ID Plan", "Coloca el ID del plan a modificar:")
        nombre_plan = simpledialog.askstring("Nuevo Nombre", "Coloca el nuevo nombre del plan:")
        
        # Agregar lógica para modificar el nombre del plan aquí
        resultado = plan.Plan.actualizarNombre(id_plan, nombre_plan)
        if resultado:
            messagebox.showinfo("Actualización", "Nombre del plan actualizado correctamente.")
        else:
            messagebox.showerror("Error", "Hubo un error al actualizar el nombre del plan. Vuelve a intentarlo.")

    def añadir_plan(self):
        nombre_plan = simpledialog.askstring("Nombre del Plan", "Coloca el nombre del nuevo plan:")
        precio_plan = simpledialog.askstring("Precio del Plan", "Coloca el precio del nuevo plan:")
        
        # Agregar lógica para añadir un nuevo plan aquí
        resultado = plan.Plan.crear(nombre_plan, precio_plan)
        if resultado:
            messagebox.showinfo("Creación", "Nuevo plan creado correctamente.")
        else:
            messagebox.showerror("Error", "Hubo un error al crear el nuevo plan. Vuelve a intentarlo.")

    def mostrar_planes(self):
        # Agregar lógica para mostrar los planes aquí
        mostrar = plan.Plan.mostrar()
        if mostrar:
            info = "\n".join(f"Id del plan: {fila[0]} - Nombre: {fila[1]} - Precio: {fila[2]}" for fila in mostrar)
            messagebox.showinfo("Planes", info)
        else:
            messagebox.showwarning("No Encontrado", "No existen planes para mostrar.")

    def modificar_clientes(self):
        self.clear_window()

        tk.Label(self.root, text="..:: Modificar Clientes ::..").pack()
        tk.Button(self.root, text="Modificar Datos", command=self.modificar_datos_cliente).pack(pady=5)
        tk.Button(self.root, text="Agregar Cliente", command=self.agregar_cliente).pack(pady=5)
        tk.Button(self.root, text="Volver", command=self.menu_empleado).pack(pady=10)

    def modificar_datos_cliente(self):
        id_cliente = simpledialog.askstring("ID Cliente", "Coloca el ID del cliente a modificar:")
        nombre = simpledialog.askstring("Nombre", "Coloca el nombre correcto:")
        apellidos = simpledialog.askstring("Apellidos", "Coloca los apellidos correctos:")
        plan = simpledialog.askstring("Plan", "Coloca el ID del plan a actualizar:")
        
        # Agregar lógica para modificar los datos del cliente aquí
        resultado = cliente.Cliente.actualizar(id_cliente, nombre, apellidos, plan)
        if resultado:
            messagebox.showinfo("Actualización", "Datos del cliente actualizados correctamente.")
        else:
            messagebox.showerror("Error", "Hubo un error al actualizar los datos del cliente. Verifica los datos.")

    def agregar_cliente(self):
        nombre = simpledialog.askstring("Nombre", "Coloca el nombre del cliente:")
        apellidos = simpledialog.askstring("Apellidos", "Coloca los apellidos del cliente:")
        plan = simpledialog.askstring("Plan", "Coloca el ID del plan:")
        
        # Agregar lógica para agregar un nuevo cliente aquí
        resultado = cliente.Cliente(nombre, apellidos, plan)
        if resultado:
            messagebox.showinfo("Creación", "Cliente creado correctamente.")
        else:
            messagebox.showerror("Error", "Hubo un error al crear el cliente. Verifica los datos.")

    def acceder_servicios(self):
        self.clear_window()

        tk.Label(self.root, text="..:: Acceder Servicios ::..").pack()
        tk.Button(self.root, text="Agregar Servicio", command=self.agregar_servicio).pack(pady=5)
        tk.Button(self.root, text="Mostrar Servicios", command=self.mostrar_servicios).pack(pady=5)
        tk.Button(self.root, text="Volver", command=self.menu_empleado).pack(pady=10)

    def agregar_servicio(self):
        cliente_id = simpledialog.askstring("ID Cliente", "Coloca el ID del cliente:")
        empleado_id = simpledialog.askstring("ID Empleado", "Coloca tu ID de empleado:")
        descripcion = simpledialog.askstring("Descripción", "Coloca la descripción del servicio:")
        
        # Agregar lógica para agregar un nuevo servicio aquí
        resultado = servicio.Servicio.crear(cliente_id, empleado_id, descripcion)
        if resultado:
            messagebox.showinfo("Creación", "Servicio creado correctamente.")
        else:
            messagebox.showerror("Error", "Hubo un error al crear el servicio. Verifica los datos.")

    def mostrar_servicios(self):
        # Agregar lógica para mostrar servicios aquí
        registros = servicio.Servicio.mostrar()
        if registros:
            info = "\n".join(f"Id del servicio: {fila[0]} - Id del cliente: {fila[1]} - Id del empleado: {fila[2]} - Fecha: {fila[3]} - Descripción: {fila[4]}" for fila in registros)
            messagebox.showinfo("Servicios", info)
        else:
            messagebox.showwarning("No Encontrado", "No existen servicios para mostrar.")

    def modificar_empleados(self):
        self.clear_window()

        tk.Label(self.root, text="..:: Modificar Empleados ::..").pack()
        tk.Button(self.root, text="Acceder a Mis Datos", command=self.acceder_datos_empleado).pack(pady=5)
        tk.Button(self.root, text="Agregar Empleado", command=self.agregar_empleado).pack(pady=5)
        tk.Button(self.root, text="Volver", command=self.menu_empleado).pack(pady=10)

    def acceder_datos_empleado(self):
        id_empleado = simpledialog.askstring("ID Empleado", "Coloca tu ID de empleado:")
        
        # Agregar lógica para mostrar datos del empleado aquí
        resultado = empleados.Empleado.mostrar(id_empleado)
        if resultado:
            info = "\n".join(f"Id del empleado: {fila[0]} - Nombre: {fila[1]} - Apellidos: {fila[2]} - Puesto: {fila[3]} - Salario: {fila[4]} - Horario: {fila[5]}" for fila in resultado)
            messagebox.showinfo("Datos del Empleado", info)
        else:
            messagebox.showwarning("No Encontrado", "No existen empleados con ese ID.")

    def agregar_empleado(self):
        nombre = simpledialog.askstring("Nombre", "Coloca el nombre del empleado:")
        apellidos = simpledialog.askstring("Apellidos", "Coloca los apellidos del empleado:")
        puesto = simpledialog.askstring("Puesto", "Coloca el puesto (recepcionista/entrenador):")
        salario = simpledialog.askstring("Salario", "Coloca el salario del empleado:")
        horario = simpledialog.askstring("Horario", "Coloca el horario del empleado (matutino/vespertino):")
        
        # Agregar lógica para agregar un nuevo empleado aquí
        resultado = empleados.Empleado.crear(nombre, apellidos, puesto, salario, horario)
        if resultado:
            messagebox.showinfo("Creación", "Empleado creado correctamente.")
        else:
            messagebox.showerror("Error", "Hubo un error al crear el empleado. Verifica los datos.")

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = crear_ventana("Sistema de Gestión")
    app = App(root)
    root.mainloop()
