clientes = []

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

    for habitacion in habitaciones_disponibles:
        if habitacion["estado"] == "Disponible":
            print(f"Número: {habitacion['numero']}")
            print(f"Tipo: {habitacion['tipo']}")
            print(f"Precio: {habitacion['precio']}")
            print("---------------------")


def cancelar_reservacion():
    for habitacion in habitaciones_disponibles:
        if habitacion 

        

