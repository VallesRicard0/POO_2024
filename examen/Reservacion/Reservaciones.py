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