from paquete.inventario import agregar_equipo, mostrar_equipos,buscar_equipo, eliminar_equipo,editar_equipo


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