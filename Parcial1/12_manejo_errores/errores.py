#Los errores en u  lenguaje de programacion se presenta cuando existe una anomalia o error dentro dela ejecucion del codigo lo cual provoca que se detenga el programa, la ejecucuin del mismo, con el control y manejo de ecepciones sera posible minimisar o evitar la interrupcion del programa devido a una ecepcion

#ejemplo 1 cuando ena variable no se genera 

nombre=input("introduce el nombre completo de una persona: ")

if len(nombre)>0:
  nombre_usuario="el nombre completo del usuario es: "
print(nombre_usuario)


#Ejemplo cunado se solicita un numero y slicita otra cosa
try:
    numero=input("Ingrese un numero")

    if numero>0:
     print("Soy un numero entero positivo")
    elif numero==0:
     print("soy un numero negativo entero")
    else:
     print("Soy un numero entero negativo")
except ValueError:
   print("Intoduce un valor numerico entero")


#Ejemplo 3 cuando se generan ultiples ecepciones
try:
    numero=int(input("Introduce un numero"))
    print("El cuadrado de el numero es: " +str(numero*numero))
except ValueError:
  print("Ingresa un valor numerico entero")
except TypeError:
  print("Se debe de convertir el numero entero")
else:
  print("NO se presentaron errores de ejecucion")
finally:
  print("Termine la ejecucion")
  
