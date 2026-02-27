clientes = []

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
            print(f"Número: {habitacion['numero']}")
            print(f"Tipo: {habitacion['tipo']}")
            print(f"Precio: {habitacion['precio']}")
            print("---------------------")

    if not hay_disponibles:
        print("No hay habitaciones Disponibles")



def menu():
    while True:
        print("==BIENVENIDO==")
        print("1.Ingrese sus datos: ")
        print("2. Habitaciones Disponibles: ")
        print("3. Salir del Programa: ")

        opcion = input("Selecciona una Opcion: ")

        if opcion == "1":
            crear_cliente()
        elif opcion == "2":
            habitaciones_disponibles()
        if opcion == "3":
            "Saliendo del programa"
            break
        else:
            print("por favor ingresa una opccion valida")

menu()


        




        

