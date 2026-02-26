
estudiantes = []

def pedir_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Por Favor ingresa un valor válido")


def pedir_float(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            return valor
        except ValueError:
            print("Ingresa un Valor Válido")


def pedir_notas():
    nota1 = pedir_float("Ingrese la nota 1: ")
    nota2 = pedir_float("Ingrese la nota 2: ")
    nota3 = pedir_float("Ingrese la nota 3: ")
    promedio = (nota1 + nota2 + nota3) / 3
    
    return {
        "nota1": nota1,
        "nota2": nota2,
        "nota3": nota3,
        "promedio": promedio
    }


def registrar_estudiantes():
    nombre = input("Ingresa tu nombre: ").strip().title()
    edad = pedir_entero("Ingresa tu edad: ")
    notas = pedir_notas()

    estudiante = {
        "nombre": nombre,
        "edad": edad,
        "nota1": notas["nota1"],
        "nota2": notas["nota2"],
        "nota3": notas["nota3"],
        "promedio": notas["promedio"]
    }
    
    estudiantes.append(estudiante)
    print(" Usuario Agregado Correctamente")


def mostrar_estudiantes():
    if not estudiantes:
        print(" No hay estudiantes registrados")
        return
                        
    for i, estudiante in enumerate(estudiantes, 1):
        print(f"\n=== Estudiante {i} ===")
        print(f"Nombre: {estudiante['nombre']}")
        print(f"Edad: {estudiante['edad']}")
        print(f"Nota 1: {estudiante['nota1']}")
        print(f"Nota 2: {estudiante['nota2']}")
        print(f"Nota 3: {estudiante['nota3']}")
        print(f"Promedio: {estudiante['promedio']:.2f}")

        if estudiante["promedio"] >= 3:
            print(" Aprobaste")
        else:
            print(" Has Reprobado")


def buscar_estudiante():
    nombre_buscar = input("Ingresa el Nombre del Estudiante: ").strip().title()

    for estudiante in estudiantes:
        if estudiante["nombre"] == nombre_buscar:
            print("=== Estudiante Encontrado ===")
            print(f"Nombre: {estudiante['nombre']}")
            print(f"Edad: {estudiante['edad']}")
            print(f"Nota 1: {estudiante['nota1']}")
            print(f"Nota 2: {estudiante['nota2']}")
            print(f"Nota 3: {estudiante['nota3']}")
            print(f"Promedio: {estudiante['promedio']:.2f}")
            return
    
    print(" Estudiante no Encontrado")


def eliminar_estudiante():
    nombre_eliminar = input("Ingresa el Nombre del estudiante que vas a Eliminar: ").strip().title()

    for i, estudiante in enumerate(estudiantes):
        if estudiante["nombre"] == nombre_eliminar:
            estudiantes.pop(i)
            print("Usuario Eliminado")
            return
    
    print("Usuario no encontrado")


def editar_notas():
    nombre_editar = input("Ingrese el Nombre del estudiante que quiere actualizarle la Nota: ").strip().title()
    
    for estudiante in estudiantes:
        if estudiante["nombre"] == nombre_editar:
            print("Ingrese las nuevas Notas:")
            notas = pedir_notas()
            
            estudiante["nota1"] = notas["nota1"]
            estudiante["nota2"] = notas["nota2"]
            estudiante["nota3"] = notas["nota3"]
            estudiante["promedio"] = notas["promedio"]
            
            print("Notas actualizadas correctamente")
            return
    
    print("Estudiante no encontrado")


def mostrar_menu():
    while True:
        print("=" * 30)
        print("=== BIENVENIDO ===")
        print("=" * 30)
        print("1. Registrar estudiante")
        print("2. Mostrar estudiantes")
        print("3. Buscar estudiante")
        print("4. Eliminar estudiante")
        print("5. Editar notas")
        print("6. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            registrar_estudiantes()
        elif opcion == "2":
            mostrar_estudiantes()
        elif opcion == "3":
            buscar_estudiante()
        elif opcion == "4":
            eliminar_estudiante()
        elif opcion == "5":
            editar_notas()
        elif opcion == "6":
            print("Saliendo")
            break
        else:
            print("Opción inválida")


mostrar_menu()




