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
