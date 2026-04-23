from .datos import jugadores
def agregar_jugador():
    futbolista = input("Ingresa el Nombre del Jugador: ")
    equipo = input("Ingresa el equipo en el que juega: ")

    jugador = {
        "futbolista" : futbolista,
        "equipo" : equipo 
    }
    jugadores.append(jugador)
    print("El Jugador se agrego correctamente")

def ver_jugador():
    if not jugadores:
        print("No hay Ningun Jugardor Resgistrado")
        return
    
    ver = input("Ingresa el nombre del futbolista que quieres ver: ")

    for jugador in jugadores:
        if jugador["futbolista"].lower() == ver.lower():
            print(f"futbolista {jugador['futbolista']}")
            print(f"equipo {jugador['equipo']}")
            return

    print("Jugador no Encontardo")


def eliminar_jugador():
    if not jugadores:
        print("No hay Jugadores Ingresados")
        return 
    
    ver = input("Ingresa el Nombre del jugaador que desea eliminar: ")

    for jugador in jugadores:
        if jugador["futbolista"].lower() == ver.lower():
            jugadores.remove(jugador)
            print("El jugador fue eliminado correctamente")
            return 
        
    print("Jugador no encontrado")




    