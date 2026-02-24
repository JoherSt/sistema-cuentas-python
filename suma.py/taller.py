equipos = []

def pedir_int(mensaje):
    while True :
        try:
            return int(input(mensaje))
        except ValueError:
            print("Ingrese un dato valido: ")

def pedir_bool(mensaje):
    while True:
        valor = input(f"{mensaje} ").strip().lower()
        if valor == "si":
            return  True
        elif valor == "no":
            return False 
        else:
            print("Respuesta (Si/No)")

def agregar_equipo():
    numero_inventario = pedir_int("Ingresa el numero del Inventario: ")
    tipo_equipo = input("Ingresa el tipo de Equipo: ")
    marca = input("Ingrese la Marca del equipo: ")
    tiene_licencia = pedir_bool("Cuenta con Licencia office(Si/No): ")


    
    equipo = {
    "numero de inventario": numero_inventario,
    "tipo de equipo": tipo_equipo,
    "marca": marca,
    "tiene licencia": tiene_licencia

   
}
    equipos.append(equipo)
    print("Equipo agregado Correctamente")
    

 

def mostrar_equipo():
    if not equipos:
        print("No hay Equipos Registrados")
        return
    for equipo in equipos:
        for clave, valor in equipo.items():
            print(f"{clave}:{valor}")
            print()

def menu():
    print("== MENU INVENTARIO ==" )
    print("1.Agregar Equipo: ")
    print("2.Mostrar Equipos: ")
    print("3.Salir")

    opcion = input("Ingresa una opcion: ")

    if opcion == "1":
        agregar_equipo()
    elif opcion == "2":
        mostrar_equipo()
    elif opcion == "3":
        print("Saliste del programa")
    else:
        print("Ingrese una opcion valida")


menu()









