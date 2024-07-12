# Clases2.py

class Lectores:
    def __init__(self, nombre, direccion, tel):
        self.nombre = nombre
        self.direccion = direccion
        self.tel = tel

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_direccion(self):
        return self.direccion

    def set_direccion(self, direccion):
        self.direccion = direccion

    def get_telefono(self):
        return self.tel

    def set_telefono(self, tel):
        self.tel = tel


class Docentes(Lectores):
    def __init__(self, nombre, direccion, tel, modalidad, num_empleado):
        super().__init__(nombre, direccion, tel)
        self.modalidad = modalidad
        self.num_empleado = num_empleado

    def get_modalidad(self):
        return self.modalidad

    def set_modalidad(self, modalidad):
        self.modalidad = modalidad

    def get_num_empleado(self):
        return self.num_empleado

    def set_num_empleado(self, num_empleado):
        self.num_empleado = num_empleado

    def get_info(self):
        print(f"El nombre del docente es {self.get_nombre()}, su dirección es {self.get_direccion()}, su número es {self.get_telefono()}, su modalidad es {self.get_modalidad()} y su número de empleado es {self.get_num_empleado()}")


class Estudiantes(Lectores):
    def __init__(self, nombre, direccion, tel, carrera, matricula):
        super().__init__(nombre, direccion, tel)
        self.carrera = carrera
        self.matricula = matricula

    def get_carrera(self):
        return self.carrera

    def set_carrera(self, carrera):
        self.carrera = carrera

    def get_matricula(self):
        return self.matricula

    def set_matricula(self, matricula):
        self.matricula = matricula

    def get_info(self):
        print(f"El nombre del alumno es {self.get_nombre()}, su dirección es {self.get_direccion()}, su número de teléfono es {self.get_telefono()}, su carrera es {self.get_carrera()}, y su matrícula es {self.get_matricula()}")
