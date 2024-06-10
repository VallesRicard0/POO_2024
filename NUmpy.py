
#1. **¿Qué es NumPy?**
   #- **NumPy** (abreviatura de *Numerical Python*) es una biblioteca de Python que se utiliza para realizar **cálculos numéricos** y **manipulación de datos**.
   #- Su objetivo principal es trabajar con **arrays multidimensionales** (también conocidos como matrices) de manera eficiente.

#2. **Arrays y Matrices: ¿Por qué son importantes?**
  # - Imagina que tienes una lista de números, como [1, 2, 3, 4, 5]. Un **array** es una estructura similar, pero más poderosa.
   #- Los arrays pueden tener **múltiples dimensiones**, como una tabla o una matriz. Por ejemplo, una matriz de 2x3 tiene 2 filas y 3 columnas.
   #- Estos arrays son útiles para representar datos en ciencia, ingeniería, finanzas y más.

#3. **Operaciones Básicas con NumPy:**
   #- **Creación de Arrays:**
     #- Puedes crear un array desde una lista de números: `array = np.array([1, 2, 3])`.
   #- **Operaciones Matemáticas:**
     #- NumPy permite hacer cálculos con arrays de manera eficiente.
     #- Por ejemplo, puedes sumar dos arrays elemento por elemento: `array_a + array_b`.
   #- **Funciones Estadísticas:**
     #- Calcula la media, la desviación estándar y otros valores estadísticos con facilidad.
   #- **Indexación y Slicing:**
     #- Accede a elementos específicos de un array o crea subconjuntos.

#4. **¿Por qué usar NumPy?**
   #- **Eficiencia**: NumPy está optimizado para cálculos rápidos, lo que es crucial para grandes conjuntos de datos.
   #- **Funciones Matemáticas**: Ofrece una amplia gama de operaciones matemáticas.
   #- **Integración con Otras Bibliotecas**: Se combina bien con pandas, Matplotlib y más.













#Ejemplo 1: Creación de Arrays
import numpy as np

# Crear un array de una dimensión
array_uno = np.array([1, 2, 3, 4, 5])
print("Array de una dimensión:", array_uno)

# Crear un array de dos dimensiones (matriz)
array_dos = np.array([[1, 2, 3], [4, 5, 6]])
print("Array de dos dimensiones (matriz):")
print(array_dos)

#1. Primero, importas NumPy con `import numpy as np`.
#2. Luego, creas un **array de una dimensión** llamado `array_uno` con los valores `[1, 2, 3, 4, 5]`.
#3. Imprimes el mensaje "Array de una dimensión:" seguido de los valores de `array_uno`.
#4. A continuación, creas un **array de dos dimensiones** (una matriz) llamado `array_dos` con los valores `[[1, 2, 3], [4, 5, 6]]`.
#5. Finalmente, imprimes el mensaje "Array de dos dimensiones (matriz):" seguido de los valores de `array_dos`.














#Ejemplo 2: Operaciones Matemáticas Básicas
import numpy as np

# Suma de arrays
array_a = np.array([1, 2, 3])
array_b = np.array([4, 5, 6])
suma = array_a + array_b
print("Suma de arrays:", suma)

# Multiplicación de arrays elemento a elemento
multiplicacion = array_a * array_b
print("Multiplicación elemento a elemento:", multiplicacion)

#1. Primero, importas NumPy con `import numpy as np`.
#2. Luego, creas dos arrays: `array_a` con los valores `[1, 2, 3]` y `array_b` con los valores `[4, 5, 6]`.
#3. Realizas la **suma elemento a elemento** de `array_a` y `array_b`, lo que da como resultado `[5, 7, 9]`.
#4. Imprimes el mensaje "Suma de arrays:" seguido de los valores resultantes.
#5. A continuación, realizas la **multiplicación elemento a elemento** de `array_a` y `array_b`, lo que da como resultado `[4, 10, 18]`.
#6. Imprimes el mensaje "Multiplicación elemento a elemento:" seguido de los valores resultantes.






#Ejemplo 3: Funciones Estadísticas
import numpy as np

# Crear un array con números aleatorios
array_aleatorio = np.random.rand(10)
print("Array aleatorio:", array_aleatorio)

# Calcular la media y la desviación estándar
media = np.mean(array_aleatorio)
desviacion_estandar = np.std(array_aleatorio)
print("Media del array:", media)
print("Desviación estándar del array:", desviacion_estandar)


#1. Importas NumPy con `import numpy as np`.
#2. Creas un **array aleatorio** de 10 elementos utilizando `np.random.rand(10)`.
#3. Imprimes el mensaje "Array aleatorio:" seguido de los valores generados en `array_aleatorio`.
#4. Calculas la **media** de los valores en `array_aleatorio` utilizando `np.mean(array_aleatorio)`.
#5. Calculas la **desviación estándar** de los valores en `array_aleatorio` utilizando `np.std(array_aleatorio)`.
#6. Imprimes los resultados de la media y la desviación estándar.
