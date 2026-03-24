estudiantes = []

def pedir_int(mensaje):
    while True:
        try:
            pedir_edad = int(input(mensaje))
            return pedir_edad
        except ValueError:
            print("Debes Ingresar el tipo de valor correspondiente")
    
def agregar_estudiante():
    nombre = input("Ingresa tu Nombre: ")
    edad = pedir_int("Ingresa tu Edad: ")
    curso = input("Ingresa tu Curso: ")

    estudiante = {
        "nombre" : nombre,
        "edad" : edad,
        "curso" : curso
    }

    estudiantes.append(estudiante)
    print("Estudiante agregado Exitosamente")

def ver_estudiantes():
    if not estudiantes:
        print("No hay Ningun estudiante Registrado")
        return


    for estudiante in estudiantes:
        print(f"{estudiante['nombre']}")
        print(f"{estudiante['edad']}")
        print(f"{estudiante['curso']}")


def buscar_estudiante():
    if not estudiantes:
        print("No hay ningun estudiante Registrado")
        return

    ver = input("ingresa tu nombre: ")

    for estudiante in estudiantes:
        if estudiante["nombre"] == ver:
            print(f"Nombre: {estudiante['nombre']}")
            print(f"Edad: {estudiante['edad']}")
            print(f"Curso {estudiante['curso']}")

def eliminar_estudiante():
    if not estudiantes:
        print("No hay estudiantes Registrados: ")
        return
    
    eliminar = input("Ingresa el Nombre del estudiante que deseas eliminar: ")

    for estudiante in estudiantes:
        if estudiante['nombre'] == eliminar:
            estudiantes.remove(estudiante)
            print("Estudiante eliminado exitosamente")


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