# Inicializamos los contadores para los aprobados y los no aprobados
aprobados = 0
no_aprobados = 0

# Definimos el número de alumnos
num_alumnos = 15

# Solicitamos las calificaciones de los alumnos
for i in range(1, num_alumnos + 1):
    # Pedimos la calificación del alumno
    calificacion = float(input(f"Introduce la calificación del alumno {i}: "))
    
    # Verificamos si la calificación es aprobatoria (>= 6)
    if calificacion >= 6:
        aprobados += 1
    else:
        no_aprobados += 1

# Mostramos el resultado
print(f"\nNúmero de alumnos aprobados: {aprobados}")
print(f"Número de alumnos no aprobados: {no_aprobados}")
