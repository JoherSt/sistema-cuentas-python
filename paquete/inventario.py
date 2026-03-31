equipos = []

def pedir_entero(mensaje):
        while True:
            try:
                return int(input(mensaje))
            except ValueError:
                print(" Debes ingresar un número válido") 

def pedir_bool(mensaje):
        while True:
            valor = input(mensaje + " (Si/No): ").strip().lower()
            if valor == "si":
                return True 
            elif valor == "no":
                return False
            else:
                print(" Debes ingresar Si o No")

def agregar_equipo()    :
    print("=== Registrando un nuevo equipo ===")

    numero_inventario = pedir_entero("Ingrese el N°Inventario: ")
    numero_activo = pedir_entero("Ingrese el Número del Activo: ")
    persona_a_cargo = input("Ingrese el nombre de la persona a cargo de este equipo: ")
    usuario = input("Usuario asignado: ")
    nombre_equipo = input("Ingrese el Nombre del equipo: ")
    contraseña_equipo = input("Ingrese la Contraseña: ")
    modelo = input("Modelo: ")
    marca = input("Ingrese la Marca: ")
    serial = input("Ingrese Número de serie: ")
    modo_bios = input("Ingrese el Modo de Bios: ")
    serie_bios = input("Ingrese la Serie de Bios: ")
    procesador = input("Ingrese el Procesador: ")
    ram = pedir_entero("Ingrese la Memoria Ram: ")
    almacenamiento = pedir_entero("Ingrese el Almacenamiento del equipo: ")
    sistema_operativo = input("Ingrese el Sistema Operativo: ")
    estado = input("Estado (Activo / Inactivo): ")
    anotaciones = input("Ingrese las fallas del equipo (Opcional): ")
    valor_costo = pedir_entero("Ingrese el valor de costo del equipo: ")
    valor_comercializacion = pedir_entero("Ingrese el valor de comercialización: ")
    diferencia = valor_costo - valor_comercializacion 
    print(f"La diferencia es {diferencia}")
    tiene_office = pedir_bool("¿El equipo tiene Office instalado?") 
    tiene_windows = pedir_bool("¿El equipo tiene Windows instalado?")

    equipo = {
        "numero_inventario": numero_inventario,
        "numero_activo": numero_activo,
        "persona_a_cargo": persona_a_cargo,
        "usuario": usuario,
        "nombre_equipo": nombre_equipo,
        "contraseña_equipo": contraseña_equipo,
        "modelo": modelo,
        "marca": marca,
        "serial": serial,
        "modo_bios": modo_bios,
        "serie_bios": serie_bios,
        "procesador": procesador,
        "ram": ram,
        "almacenamiento": almacenamiento,
        "sistema_operativo": sistema_operativo,
        "estado": estado,
        "anotaciones": anotaciones,
        "valor_costo": valor_costo,
        "valor_comercializacion": valor_comercializacion,
        "tiene_office": tiene_office,
        "diferencia": diferencia,
        "tiene_windows": tiene_windows
    }

    equipos.append(equipo)
    print(" Equipo agregado correctamente ")

def mostrar_equipos():
    if not equipos:
        print(" No hay equipos registrados ")
        return

    print(" LISTA DE EQUIPOS ")
    for equipo in equipos:
        for clave, valor in equipo.items():
            print(f"{clave}: {valor}")
        print()  
def buscar_equipo():
    
    serial_buscar = input("Ingrese el serial a buscar: ")

    for equipo in equipos:
            if equipo["serial"] == serial_buscar:
                print(" Equipo encontrado: ")
                for clave, valor in equipo.items():
                    print(f"{clave}: {valor}")
                print()
                return

print(" Equipo no encontrado ")

def eliminar_equipo():
    if not equipos:
        print("No hay equipos Registrados")
        return
    
    numero = pedir_entero("Por favor ingresa el activo que deseas eliminar: ")

    print("Lista de equipos")
    for equipo in equipos:
        if equipo["numero_activo"] == numero:
            equipos.remove(equipo)
            print("el quipo se elimino Correctamente")
            return
        print("No hay equipos Registrados")


def editar_equipo():
    if not equipos:
        print("No hay equipos registrados.")
        return

    numero = pedir_entero("Ingresa el numero_activo del equipo a editar: ")

    for equipo in equipos:
        if equipo["numero_activo"] == numero:

            print(" Equipo encontrado. Datos actuales: ")
            for clave, valor in equipo.items():
                print(f"{clave}: {valor}")

            print("Escribe el Nuevo valor o presiona ENTER para dejarlo igual.")

            for clave in equipo:
                if clave == "diferencia":
                    continue  

                nuevo_valor = input(f"{clave} ({equipo[clave]}): ")

                if nuevo_valor:
                    if clave in ["numero_inventario", "numero_activo", "valor_costo", "valor_comercializacion"]:
                        equipo[clave] = int(nuevo_valor)
                    elif clave in ["tiene_office", "tiene_windows"]:
                        equipo[clave] = nuevo_valor.lower() == "si"
                    else:
                        equipo[clave] = nuevo_valor

            
            equipo["diferencia"] = equipo["valor_comercializacion"] - equipo["valor_costo"]

            print(" Equipo actualizado correctamente.")
            return

    print(" No se encontró un equipo con ese numero.")


def menu():
    while True:
        print("==== MENÚ INVENTARIO ====")
        print("1. Agregar equipo")
        print("2. Mostrar equipos")
        print("3. Buscar equipo por serial")
        print("4. Eliminar Equipo")
        print("5. Editar")
        print("6. Salir")

        opcion = input(" Seleccione una opción: ")

        if opcion == "1":
            agregar_equipo()
        elif opcion == "2":
            mostrar_equipos()
        elif opcion == "3":
            buscar_equipo()
        elif opcion == "4":
            eliminar_equipo()
        elif opcion == "5":
            editar_equipo()
        elif opcion == "6":
            print("Saliendo del programa")
            break
        else:
            print(" Opción no válida ")

menu()
