from paquete.registro_banco import registro, iniciar_sesion, mostrar_cuenta, pedir_monto
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