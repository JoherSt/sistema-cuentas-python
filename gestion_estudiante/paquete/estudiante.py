from .datos import estudiantes
from .utils import pedir_int

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
        else:
            print("Este usuario no existe: ")    

def eliminar_estudiante():
    if not estudiantes:
        print("No hay estudiantes Registrados: ")
        return
    
    eliminar = input("Ingresa el Nombre del estudiante que deseas eliminar: ")

    for estudiante in estudiantes:
        if estudiante['nombre'] == eliminar:
            estudiantes.remove(estudiante)
            print("Estudiante eliminado exitosamente")


