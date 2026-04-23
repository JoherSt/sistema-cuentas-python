from paquete.inicio_sesion import crear_cuenta, iniciar_sesion, menu_usuario

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