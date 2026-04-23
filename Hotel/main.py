from paquete.hotel import crear_cliente, habitaciones_disponibles, reservar_habitacion

def menu():
    while True:
        print("==BIENVENIDO==")
        print("1.Ingrese sus datos: ")
        print("2. Habitaciones Disponibles: ")
        print("3. Reservar Habitacion: ")
        print("4. Salir: ")

        opcion = input("Selecciona una Opcion: ")

        if opcion == "1":
            crear_cliente()
        elif opcion == "2":
            habitaciones_disponibles()
        elif opcion == "3":
            reservar_habitacion()
        elif opcion == "4":
            "Saliendo del programa"
            break
        else:
            print("por favor ingresa una opccion valida")

menu()