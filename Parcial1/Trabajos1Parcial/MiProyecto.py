def sevastopol():
    import os

    DDB = [""] * 100
    Limpz = 24
    PRSN = 104
    RMA = 0
    IV = 0
    C1 = 0

    print("                                      Bienvenido a Sevastopol")

    while True:
        IV += 1
        print("                                    ----- Menú Principal -----")
        print("                                    1- Registrar nuevo huésped")
        print("                                   2- Mostrar lista de huéspedes")
        print("                                    3- Buscar huésped por nombre")
        print("                                         4- Salir al menú")
        print("                               Seleccione una opción para continuar")
        CFG0 = int(input())
        os.system('cls' if os.name == 'nt' else 'clear')

        if CFG0 == 1:
            print("                                Nombre completo")
            CN = input()
            print("                           Fecha de ingreso (DD/MM/AAAA)")
            EF = input()
            print("                           Fecha de despacho (DD/MM/AAAA)")
            SF = input()
            C1 += 1
            DDB[C1] = CN
            print(f"                                      ¿Qué habitación desea alquilar? {CN}")
            print("1- Individual: Para una persona que incluye lo básico requerido (1-Cama, 1-Baño), 3 días por $1,000")
            print("2- Matrimonial: Para dos personas que incluye lo básico requerido (1-Cama Matrimonial, 1-Baño), 3 días por $2,000")
            print("3- Pijamada: Para tres personas que incluye lo básico requerido (3-Camas individuales, 1-Baño), 3 días por $3,500")
            print("4- Familiar: Para cuatro personas que incluye lo básico requerido (2-Camas Matrimoniales, 1-Cama individual, 2-Baños), 3 días por $5,000")
            print("5- Presidencial: Para cinco personas o más que incluye servicios de lujo (Vista libre en el último piso, 3-Camas Matrimoniales, 3-Camas Individuales, 4-Baños) 3 días $10,000")
            print("Nota; Todas las opciones sin importar incluyen, servicio a la habitación, acceso a la piscina, acceso al patio de juegos, acceso a los servicios de comida entre otras cosas")
            CFG2 = int(input())
            os.system('cls' if os.name == 'nt' else 'clear')

            if CFG2 == 1:
                D = 1000
                H = "Individual"
                while True:
                    print("        ¿Cuántas personas ocuparán la habitación? ")
                    NPers = int(input())
                    if NPers == 1:
                        print("   Escriba la cantidad en número que pagará (recuerde que su precio son $1000) ")
                        TP = float(input())
                        D1 = D - (TP - Limpz)
                        if D1 >= 0:
                            print("    Usted ha pagado y este es su cambio = $", D1)
                            break
                        else:
                            print("     Su pago no es suficiente, por favor vuelva a ingresar los datos ")
                    elif NPers > 1:
                        print("    Se cobrará un impuesto por ser más personas de las que se permiten (NP * $104) ")
                        Tpers = NPers * PRSN
                        D11 = D + Tpers + Limpz
                        print("         Su nuevo pago será el siguiente  $", D11)
                        print("        Escriba la cantidad en número que pagará")
                        TP = float(input())
                        D1 = TP - D11
                        if D1 >= 0:
                            print("    Usted ha pagado y este es su cambio = $", D1)
                            break
                        else:
                            print(" Su pago no es suficiente, por favor vuelva a ingresar los datos ")

                print("ATENCION!! Al alquilar la habitación ha aceptado nuestras políticas de privacidad!!")
                print(CN, " Usted alquiló una habitación el día ", EF, " con caducidad al día ", SF, " con una habitación de tipo ", H)
                print("Gracias por preferir Sevastopol que tenga un buen día ", CN)
                os.system('cls' if os.name == 'nt' else 'clear')
            
            elif CFG2 == 2:
                D = 2000
                H = "Matrimonial con precio de $2,000"
                while True:
                    print(" ¿Cuántas personas ocuparán la habitación? ")
                    NPers = int(input())
                    if NPers <= 2:
                        print("Escriba la cantidad en número que pagará", H)
                        TP = float(input())
                        D1 = D - (TP - Limpz)
                        if D1 >= 0:
                            print("Usted ha pagado y este es su cambio = $", D1)
                            break
                        else:
                            print("Su pago no es suficiente, por favor vuelva a ingresar los datos ")
                    elif NPers > 2:
                        print(" Se cobrará un impuesto por ser más personas de las que se permiten (NP * $104) ")
                        Tpers = NPers * PRSN
                        D11 = D + Tpers + Limpz
                        print("Su nuevo pago será el siguiente  $", D11)
                        print("Escriba la cantidad en número que pagará")
                        TP = float(input())
                        D1 = TP - D11
                        if D1 >= 0:
                            print("Usted ha pagado y este es su cambio = $", D1)
                            break
                        else:
                            print(" Su pago no es suficiente, por favor vuelva a ingresar los datos ")

                print("ATENCION!! Al alquilar la habitación ha aceptado nuestras políticas de privacidad!!")
                print(CN, " Usted alquiló una habitación el día ", EF, " con caducidad al día ", SF, " con una habitación de tipo ", H)
                print("Gracias por preferir Sevastopol que tenga un buen día ", CN)

            elif CFG2 == 3:
                D = 3500
                H = "Pijamada con precio de $3,500"
                while True:
                    print(" ¿Cuántas personas ocuparán la habitación? ")
                    NPers = int(input())
                    if NPers <= 3:
                        print("Escriba la cantidad en número que pagará", H)
                        TP = float(input())
                        D1 = D - (TP - Limpz)
                        if D1 >= 0:
                            print("Usted ha pagado y este es su cambio = $", D1)
                            break
                        else:
                            print("Su pago no es suficiente, por favor vuelva a ingresar los datos ")
                    elif NPers > 3:
                        print(" Se cobrará un impuesto por ser más personas de las que se permiten (NP * $104) ")
                        Tpers = NPers * PRSN
                        D11 = D + Tpers + Limpz
                        print("Su nuevo pago será el siguiente  $", D11)
                        print("Escriba la cantidad en número que pagará")
                        TP = float(input())
                        D1 = TP - D11
                        if D1 >= 0:
                            print("Usted ha pagado y este es su cambio = $", D1)
                            break
                        else:
                            print(" Su pago no es suficiente, por favor vuelva a ingresar los datos ")

                print("ATENCION!! Al alquilar la habitación ha aceptado nuestras políticas de privacidad!!")
                print(CN, " Usted alquiló una habitación el día ", EF, " con caducidad al día ", SF, " con una habitación de tipo ", H)
                print("Gracias por preferir Sevastopol que tenga un buen día ", CN)

            elif CFG2 == 4:
                D = 5000
                H = "Familiar con precio de $5,000"
                while True:
                    print(" ¿Cuántas personas ocuparán la habitación? ")
                    NPers = int(input())
                    if NPers <= 4:
                        print("Escriba la cantidad en número que pagará", H)
                        TP = float(input())
                        D1 = D - (TP - Limpz)
                        if D1 >= 0:
                            print("Usted ha pagado y este es su cambio = $", D1)
                            break
                        else:
                            print("Su pago no es suficiente, por favor vuelva a ingresar los datos ")
                    elif NPers > 4:
                        print(" Se cobrará un impuesto por ser más personas de las que se permiten (NP * $104) ")
                        Tpers = NPers * PRSN
                        D11 = D + Tpers + Limpz
                        print("Su nuevo pago será el siguiente  $", D11)
                        print("Escriba la cantidad en número que pagará")
                        TP = float(input())
                        D1 = TP - D11
                        if D1 >= 0:
                            print("Usted ha pagado y este es su cambio = $", D1)
                            break
                        else:
                            print(" Su pago no es suficiente, por favor vuelva a ingresar los datos ")

                print("ATENCION!! Al alquilar la habitación ha aceptado nuestras políticas de privacidad!!")
                print(CN, " Usted alquiló una habitación el día ", EF, " con caducidad al día ", SF, " con una habitación de tipo ", H)
                print("Gracias por preferir Sevastopol que tenga un buen día ", CN)

            elif CFG2 == 5:
                D = 10000
                H = "Presidencial con precio de $10,000"
                while True:
                    print("Escriba la cantidad en número que pagará", H)
                    TP = float(input())
                    D -= TP
                    if D <= 0:
                        print("Usted ha pagado y este es su cambio = $", abs(D))
                        break
                    else:
                        print("Usted falta a pagar")
                
                print("ATENCION!! Al alquilar la habitación ha aceptado nuestras políticas de privacidad!!")
                print(CN, " Usted alquiló una habitación el día ", EF, " con caducidad al día ", SF, " con una habitación de tipo ", H)
                print("Gracias por preferir Sevastopol que tenga un buen día ", CN)

        elif CFG0 == 2:
            print("------------------------------")
            print("----- Lista de Huéspedes -----")
            for i in range(1, C1 + 1):
                print(DDB[i])
            print("------------------------------")
            print("")

        elif CFG0 == 3:
            while True:
                print("Dame un nombre para buscarlo")
                CN = input()
                F = False
                for i in range(1, C1 + 1):
                    if DDB[i] == CN:
                        F = True
                        break
                if F:
                    print(f"El huésped {CN} se encuentra en la lista.")
                else:
                    print(f"El huésped {CN} no se encuentra en la lista.")
                
                print("¿Desea volver a buscar? (Si/No)")
                CFG1 = input()
                if CFG1.lower() == "no":
                    break

        elif CFG0 == 4:
            break

    print("Gracias por utilizar el programa")

sevastopol()
