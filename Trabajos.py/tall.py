import getpass

cuentas = []

def pedir_int(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Por favor ingresa un valor válido.")


def pedir_correo(mensaje):
    while True:
        correo = input(mensaje).strip().lower()
        if "@gmail.com" in correo:
            return correo
        else:
            print("El correo debe contener @gmail.com")


def pedir_contraseña(mensaje):
    while True:
        contraseña = getpass.getpass(mensaje)
        confirmar = getpass.getpass("Confirma la contraseña: ")

        if contraseña == confirmar:
            return contraseña
        else:
            print("Las contraseñas no coinciden.")



def crear_cuenta():
    print("=== CREAR CUENTA ===")

    nombre = input("Ingresa tu Nombre: ").strip().title()
    documento = pedir_int("Ingresa tu Documento: ")
    contraseña = pedir_contraseña("Ingresa la Contraseña: ")
    edad = pedir_int("Ingresa tu Edad: ")
    telefono = pedir_int("Ingresa tu Teléfono: ")
    correo_electronico = pedir_correo("Ingresa tu Correo Electrónico: ")
    direccion = input("Ingresa tu Dirección: ").strip()

    cuenta = {
        "Nombre": nombre,
        "Documento": documento,
        "Contraseña": contraseña,
        "Edad": edad,
        "Telefono": telefono,
        "Correo": correo_electronico,
        "Direccion": direccion
    }

    cuentas.append(cuenta)
    print(" Usuario agregado con éxito.")


def iniciar_sesion():
    if not cuentas:
        print("No hay cuentas registradas. Crea una cuenta primero.")
        return None

    print("=== INICIAR SESIÓN ===")

    usuario_ingresado = input("Ingrese su Nombre: ").strip().title()
    contraseña_ingresada = getpass.getpass("Ingrese la contraseña: ")

    for cuenta in cuentas:
        if cuenta["Nombre"] == usuario_ingresado and cuenta["Contraseña"] == contraseña_ingresada:
            print(" Inicio de sesión exitoso.")
            return cuenta

    print(" Usuario o contraseña incorrectos.")
    return None


def menu_usuario(cuenta):
    while True:
        print("=== MENÚ USUARIO ===")
        print("1. Ver datos de la cuenta")
        print("2. Cerrar sesión")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            print(f"Nombre: {cuenta['Nombre']}")
            print(f"Documento: {cuenta['Documento']}")
            print(f"Edad: {cuenta['Edad']}")
            print(f"Teléfono: {cuenta['Telefono']}")
            print(f"Correo: {cuenta['Correo']}")
            print(f"Dirección: {cuenta['Direccion']}")

        elif opcion == "2":
            print("Sesión cerrada.")
            break

        else:
            print("Opción inválida.")




def menu_principal():
    cuenta_actual = None

    while True:
        print("=== BIENVENIDO ===")
        print("1. Crear Cuenta")
        print("2. Iniciar Sesión")
        print("3. Menú Usuario")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            crear_cuenta()

        elif opcion == "2":
            cuenta_actual = iniciar_sesion()

        elif opcion == "3":
            if cuenta_actual:
                menu_usuario(cuenta_actual)
            else:
                print("Primero debes iniciar sesión.")

        elif opcion == "4":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida.")




menu_principal()