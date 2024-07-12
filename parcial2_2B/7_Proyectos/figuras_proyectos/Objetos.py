# script_principal.py

from Clases2 import Estudiantes, Docentes

print("Estudiante 1")
Estudiante1 = Estudiantes("Ana Torres Guzman", "Col. Centro 1500", "6181235678", "MECA", "23355678")
Estudiante1.get_info()

print("Docente 1")
Docente1 = Docentes("Daniel Fuentes Loera", "Fracc. Arrieta 1400", "6183335678", "TI", "123")
Docente1.get_info()
