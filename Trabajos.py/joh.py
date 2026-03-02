equipos = []

def pedir_int(mensaje):
    while True:
        try:
           valor = int(input(mensaje))
           return valor
        except ValueError:
            print("Por favor Ingresa un valor valido")     

def agregar_equipos():
    nombre = input("Por favor Ingresa tu Nombre: ").title().upper()
    codigo = input("Ingresa el codigo: ")
    marca = input("Ingresa la Marca: ")
    ram = pedir_int("Ingresa la Ram: ")
    almacenamiento = pedir_int("Ingresa el almacenamiento: ")

    equipo = {
        "nombre" : nombre,
        "codigo" : codigo,
        "marca" : marca,
        "ram" : ram,
        "almacenamiento" : almacenamiento
    }

    equipos.append(equipo)
    print("El equipo se ha agregado correctamente")

def listar_equipos():
        if not equipos:
            print("No hay equipos registrados")
            return
            
        for equipo in equipos:
            print(f"codigo {equipo['codigo']}")
            print(f"marca {equipo['marca']}")
            print(f"ram {equipo['ram']} GB")
            print(f"almacenamiento {equipo['almacenamiento']} GB")
            return 
        
def buscar_codigo():
        if not equipos:
            print("No hay equipos registrados")
            return
        
        codigo = input("Ingresa el codigo para buscar el equipo: ")
        
        for equipo in equipos:
            if equipo['codigo'] == codigo:
                print(f"Se encontro el equipo: {codigo}")
                print(equipo)
                return
            else:
                print("No se encontro ningun Equipo con este codigo: ")
                break


def editar_equipo():
    if not equipos:
        print("No se ha encontrado Ningun Equipo Registrado")
        return
    
    codigo = input("Ingresa el codigo para Editar: ")

    for equipo in equipos:
        if equipo["codigo"] == codigo:
            print("Equipo Encontrado")
            print(f"codigo {equipo['codigo']}")
            print(f"marca {equipo['marca']}")
            print(f"ram {equipo['ram']} GB")
            print(f"almacenamiento {equipo['almacenamiento']} GB(SDD)")
                
            equipo["codigo"] = input("Ingresa el nuevo codigo: ")
            equipo["marca"] = input("Ingresa la Nueva Marca: ")
            equipo["ram"] = pedir_int("Ingresa la Nueva Ram: ")
            equipo["almacenamiento"] = pedir_int("Ingresa el Nuevo Almacenamiento: ")

            print("Equipo agregado correctamente")
            return
        
def eliminar():
    if not equipos:
        print("No hay ningun equipo agregado")      
        return
    
    codigo = input("Ingresa el codigo que deseas eliminar: ")

    for equipo in equipos:
        if equipo["codigo"] == codigo:
            equipos.remove(equipo)
            print("El equipo fue Eliminado Exitosamente")
            return
    else:
        print("No se Encontro Ningun Equipo con este codigo")

        
        





def menu():
    while True:
        print("==BENVENUTO==")
        print("1.Agregar Equipos: ")
        print("2.Mostrar Equipos: ")
        print("3.Buscar Equipo: ")
        print("4.Editar Equipo: ")
        print("5.Eliminar Equipo: ")
        print("6.Salir del Programa: ")

        opcion = input("Selecciona una Opcion: ")

        if opcion == "1":
            agregar_equipos()
        elif opcion == "2":
            listar_equipos()
        elif opcion == "3":
            buscar_codigo()
        elif opcion == "4":
            editar_equipo()
        elif opcion == "5":
            eliminar()
        elif opcion == "6":
            print("Saliendo del Programa: ")
            break

menu()





