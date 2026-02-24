
estudiantes = []

def pedir_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Por Favor ingresa un valor valido")


def pedir_float(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            return valor
        except ValueError:
            print("Ingresa un Valor Valido")



            


def registrar_estudiantes():
    nombre = input("Ingresa tu nombre: ")
    edad = pedir_entero("Ingresa tu edad: ") 
    nota1 = pedir_float("Ingrese la nota 1: ") 
    nota2 = pedir_float("Ingrese la nota 2: ") 
    nota3 = pedir_float("Ingrese la nota 3: ") 
    promedio =( nota1 + nota2 + nota3) / 3

    estudiante = {
    "nombre" : nombre,
    "edad" : edad,
    "nota1" : nota1,
    "nota2" :nota2,
    "nota3" :nota3,
    "promedio": promedio



}
    
    estudiantes.append(estudiante)
    print("Usuario Agregado Correctamente: ")

def mostar_estudiante():
    if not estudiantes:
        print("No hay equipos registrados")
        return
                    
    for estudiante in estudiantes:
    
                print("Nombre:", estudiante["nombre"])
                print("Edad:", estudiante["edad"])
                print("Promedio:", estudiante["promedio"])

                if estudiante["promedio"] >= "3":
                    print("Aprobaste")
                elif estudiante["promedio"] < "3":
                    print("Has reprobado")
    

def menu():
    while True:
            print("==BIENVENIDO==")
            print("1.registrar estudiante: ")
            print("2.Mostrar Estudiante: ")
            print("3.Salir: ")

            opcion = input("Selecciona Una Opcion: ")

            if opcion == "1":
                registrar_estudiantes()
            elif opcion == "2":
                mostar_estudiante()
            elif opcion == "3":
                print("Salir del programa: ")
                break


menu()




