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