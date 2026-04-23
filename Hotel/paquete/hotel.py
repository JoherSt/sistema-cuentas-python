from .datos import clientes, habitaciones, reservas
from .utils import pedir_int





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




        




        

