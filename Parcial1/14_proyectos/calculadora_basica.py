import math

def sumar(num1, num2):
    return num1 + num2

def restar(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    if num2 == 0:
        return "Error: No se puede dividir por cero"
    else:
        return num1 / num2

def potencia(num1, num2):
    return num1 ** num2

def raiz(num1, num2):
    if num2 == 0:
        return "Error: El índice de la raíz no puede ser cero"
    else:
        return num1 ** (1/num2)

opcion = ""
while opcion != "6":
    print("\nCalculadora básica")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Potencia")
    print("6. Raíz")
    print("7. Salir")

    opcion = input("Selecciona una opción (1/2/3/4/5/6/7): ")

    if opcion in ['1', '2', '3', '4', '5', '6']:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))

        if opcion == '1':
            resultado = sumar(num1, num2)
            print(f"El resultado de la suma es: {resultado}")
        elif opcion == '2':
            resultado = restar(num1, num2)
            print(f"El resultado de la resta es: {resultado}")
        elif opcion == '3':
            resultado = multiplicar(num1, num2)
            print(f"El resultado de la multiplicación es: {resultado}")
        elif opcion == '4':
            resultado = dividir(num1, num2)
            if isinstance(resultado, str):
                print(resultado)
            else:
                print(f"El resultado de la división es: {resultado}")
        elif opcion == '5':
            resultado = potencia(num1, num2)
            print(f"El resultado de la potencia es: {resultado}")
        elif opcion == '6':
            resultado = raiz(num1, num2)
            if isinstance(resultado, str):
                print(resultado)
            else:
                print(f"El resultado de la raíz es: {resultado}")
    elif opcion == "7":
        print("Saliendo del programa...")
    else:
        print("Opción no válida")