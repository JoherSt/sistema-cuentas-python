clientes = []
reservas = []

habitaciones =[
        {"estado": "Disponible", "numero": 101, "tipo" : "sencilla", "precio" : 100000},
        {"estado": "Disponible", "numero": 102, "tipo" : "doble", "precio" : 150000},
        {"estado": "Disponible", "numero": 103, "tipo" : "sencilla", "precio" : 100000},
        {"estado": "Ocupada", "numero": 104, "tipo" : "doble", "precio" : 150000}
    ]


def pedir_int(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Por favor Ingresa el Tipo de Dato Correspondiente")



def crear_cliente():
    documento = pedir_int("Ingresa tu Documento: ")
    nombre = input("Ingresa tu Nombre: ")
    telefono = pedir_int("Ingresa tu telefono: ")

    cliente = {
        "documento" : documento,
        "nombre" : nombre,
        "telefono" : telefono
    }

    clientes.append(cliente)
    print("Cliente registrado")


def habitaciones_disponibles():

    hay_disponibles = False

    for habitacion in habitaciones:
        if habitacion["estado"] == "Disponible":
            hay_disponibles = True
            print(f" número: {habitacion['numero']}")
            print(f" Tipo: {habitacion['tipo']}")
            print(f" Precio: {habitacion['precio']}")
            print("---------------------")

    if not hay_disponibles:
        print("No hay habitaciones Disponibles")


def reservar_habitacion():
    hay_disponibles = False
    for habitacion in habitaciones:
        if habitacion["estado"] == "Disponible":
            hay_disponibles = True
            break       
    
    if not hay_disponibles:
        print("No hay habitaciones disponibles")
        return
    numero = pedir_int("Ingresa el numero de la habitacion a reservar: ")

    encontrada = False

    for habitacion in habitaciones:
        if habitacion ["numero"] == numero:
            encontrada = True   

            if habitacion["estado"] != "Disponible":
                print("La Habitacion no esta Disponible")
                return
            
            
            documento = pedir_int("Ingresa tu documento: ")
            noches = pedir_int("Numero de Noches: ")
            total = noches * habitacion["precio"]

            reserva = {
                "documento": documento,
                "habitacion": habitacion,
                "noches" : noches,
                "total" : total

            }

            reservas.append(reserva)
            habitacion["estado"] = "Ocupada"

            print("Reserva realizada con exito: ")
            print(f"El total es: {total}")
            return
    if not encontrada:
            print("La habitacion no existe")

def menu():
    while True:
        print("==BIENVENIDO==")
        print("1.Ingrese sus datos: ")
        print("2. Habitaciones Disponibles: ")
        print("3. Reservar Habitacion: ")
        print("4. Salir del Programa: ")

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


        




        

