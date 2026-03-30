cuentas = []

def pedir_int(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Por favor ingresa un valor valido: ")

def pedir_correo(mensaje): 
    while True: 
            correo = input(mensaje)
            
            if "@gmail.com" in correo:
                return correo
            else:
                print("El correo debe llevar @gmail.com")

import getpass

def pedir_contraseña(mensaje):
    while True:
        contraseña = getpass.getpass(mensaje)
        confirmar = getpass.getpass("Confirma la contraseña: ")

        if contraseña == confirmar:
            return contraseña
        else: 
            print("Las Contraseñas no coinciden")

        

def crear_cuenta():
    nombre = input("Ingresa tu Nombre: ").strip().title()
    documento = pedir_int("Ingresa tu Documento: ")
    contraseña = pedir_contraseña("Ingresa la Contraseña: ")
    edad = pedir_int("Ingresa tu Edad: ")
    telefono = pedir_int("Ingresa tu Telefono: ")
    correo_electronico = pedir_correo("Ingresa tu Correo Electronico: ")
    direccion = input("Ingresa tu direccion: ")

    cuenta = {
        "Nombre" : nombre,
        "Documento" : documento,
        "Contraseña" : contraseña,
        "Edad" : edad,
        "Telefono" : telefono,
        "correo_electronico" : correo_electronico,
        "Direccion" : direccion 
    }

    cuentas.append(cuenta)
    print("Usuario Agregado con Exito")


def iniciar_sesion():
    while True:
        if not cuentas:
            print("No hay cuentas registradas. Crea una cuenta primero.")
            return None
        
        usuario_ingresado = input("Ingrese su Usuario: ")
        contraseña_ingresada = input("Ingrese la contraseña: ")
        
        for cuenta in cuentas:
            if cuenta["Nombre"] == usuario_ingresado and cuenta["Contraseña"] == contraseña_ingresada:
                print("Usuario Ingresado Correctamente")
                return cuenta
        
        print("Usuario o Contraseña Incorrectos")
def menu_cuenta(cuenta):
    while True:
        print("1.Mirar datos de la cuenta: ")
        print("2.Cerrar Sesion: ")

        opcion = input("Selecciona una opcion")

        if opcion == "1":
            print(f"Nombre: {cuenta['Nombre']}")
            print(f"Documento: {cuenta['Documento']}")
            print(f"Contraseña: {cuenta['Contraseña']}")
            print(f"Telefono: {cuenta['Telefono']}")
            print(f"Edad: {cuenta['Edad']}")
            print(f"Correo: {cuenta['correo_electronico']}")
            print(f"Direccion {cuenta['Direccion']}")

        elif opcion == "2":
            print("Saliendo de la cuenta")
            break
        else:
            print("Ingresa una opcion valida")


def menu():
    cuenta_actual = None
    while True:
        print("==BIENVENIDO==")
        print("1.Crear Cuenta: ")
        print("2.Iniciar Sesion: ")
        print("3.Menu  Cuenta: ")
        print("4.Cerrar Sesion: ")



        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            crear_cuenta()
        elif opcion == "2":
            cuenta_actual = iniciar_sesion()
        elif opcion == "3":
            if cuenta_actual:
                menu_cuenta(cuenta_actual)
            else:
                print("Debes iniciar sesion primero")
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Ingresa una Opcion valida")

menu()




        
