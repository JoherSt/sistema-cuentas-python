from paquete.estudiante import agregar_estudiante, ver_estudiantes, buscar_estudiante,eliminar_estudiante

def menu():
    while True:
        print("==BIENVENIDO==")
        print("1.Agreagar Estudiante: ")
        print("2.Ver Estudiantes: ")
        print("3.Buscar Estudiante: ") 
        print("4.Eliminar Estudiante: ")
        print("5.Salir: ")

        opcion = input("Elige una Opcion: ")

        if opcion == "1":
            agregar_estudiante()
        elif opcion == "2":
            ver_estudiantes()
        elif opcion == "3":
            buscar_estudiante()
        elif opcion == "4":
            eliminar_estudiante()
        elif opcion == "5":
            print("Saliendo del programa")
            break



menu()