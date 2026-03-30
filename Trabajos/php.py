cuentas = []

def pedir_int(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Por favor Ingresa el tipo de dato Solicitado")

def pedir_float(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            return
        except ValueError:
            print("Por favor Ingresa un valor valido")

def registro():
    nombre = input("Ingresa tu nombre de Usuario: ").lower().strip()
    contraseña = input("Ingresa tu contraseña: ").strip()
    tarjeta = pedir_int("Por favor Ingresa tu tarjeta: ")
    tipo_cuenta = input("Ingresa el tipo de cuenta: (Ahorros/Corriente): ").lower()

    if tipo_cuenta == "ahorros":
        print("Cuenta de Ahorros Seleccionada")
    elif tipo_cuenta == "corriente":
        print("Cuenta corriente seleccionada: ")


    cuenta = {
        "nombre" : nombre,
        "contraseña" : contraseña,
        "tarjeta" : tarjeta,
        "tipo_cuenta" : tipo_cuenta
    }

    cuentas.append(cuenta)
    print("Cuenta agregada exitosamente")

def iniciar_sesion():
    while True:
        if not cuentas:
            print("No hay ninguna cuenta agregada")
            return

        nombre = input("Ingresa tu nombre: ").lower().strip()
        contraseña = input("Ingresa tu contraseña: ").lower().strip()

        for cuenta in cuentas:
            if cuenta["nombre"] == nombre and cuenta["contraseña"] == contraseña:
                print("Inicio de sesion Exitoso")
                return 
        print("Nombre o Contraseña Incorrectos")

def mostrar_cuenta():
    if not cuentas:
        print("No hay cuentas Registradas: ")
        return
    
    nombre = input(" Por favor Ingresa el nombre de la Cuenta: ").lower().strip()
    
    encontrada = False
    for cuenta in cuentas:
        if cuenta["nombre"] == nombre:
            print(f"nombre {cuenta['nombre']}")
            print(f"tarjeta {cuenta['tarjeta']}")
            print(f"Tipo de Cuentas {cuenta['tipo_cuenta']}")
            encontrada = True
            break
    
    if not encontrada:
        print("No existe cuenta con este nombre")



def pedir_monto():
    while True:
        print("==SELECCIONA EL MONTO QUE QUIERES RETIRAR==")
        print("1.10.000: ")
        print("2.20.000: ")
        print("3.50.000: ")
        print("4.100.000: ")
        print("5.Otro valor: ")

        opcion = input("Selecciona una de las opciones para retirar: ")
        
        if opcion == "1":
            monto = 10.000
        elif opcion == "2":
            monto = 20.000
        elif opcion == "3":
            monto = 50.000
        elif opcion == "4":
            monto = 100.000
        elif opcion == "5":
            monto = pedir_float("Ingresa el monto que quieres retirar: ")
        else:
            print("Ingresa un valor valido: ")
            break
        print(f"Monto Retirado: {monto}")


def menu():
    while True:
        print("==BIENVENIDO==")
        print("1.Registrarse: ")
        print("2.Iniciar Sesion ")
        print("3.Mostrar Cuenta")
        print("4.Pedir Monto: ")
        print("5.Salir")

        opcion = input("Por favor Selecciona una opcion: ")

        if opcion == "1":
            registro()
        elif opcion == "2":
            iniciar_sesion()
        elif opcion == "3":
            mostrar_cuenta()
        elif opcion == "4":
            pedir_monto()
        elif opcion == "5":
            print("Saliendo del programa")
            break


menu()


             


