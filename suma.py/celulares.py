equipos = []

def pedir_entero(mensaje):
    while True:
        try: 
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Por favor ingresa un valor correcto")

def pedir_float(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            return valor 
        except ValueError:
            print("Por favor ingresa un valor correspondiente")


def pedir_bool(mensaje):
    while True:
            valor = input(mensaje +"(Si/No): ").strip().lower()
            if valor == "si":
                return True
            elif valor == "no":
                return False
            else:
                print("Por favor ingresa la respusta correcta: ")

def agregar_equipo():
    numero_inventario = pedir_entero("Ingresa el numero del inventario: ")
    numero_activo =  pedir_entero("Ingresa el numero del activo: ")
    area = input("Ingresa el Area: ")
    persona_a_cargo = input("Ingresa el Nombre de la persona a cargo de este equipo: ")
    usuario = input("Ingresa el Usuario: ")
    nombre_equipo = input("Ingresa el nombre del equipo: ")
    numero_serie = input("ingresa el numero de serie del equipo: ")
    marca = input("Por favor Ingresa la Marca: ")   
    modelo_comercial = input("Ingresa El Modelo: ")
    modelo_fabricante = input("Ingresa el modelo del fabricante(Opcional)")
    imei = input("Ingresa el Imei del Equipo: ")
    procesador = input("Ingresa el procesador del equipo: ")
    ram = pedir_entero("Ingresa la memoria RAM: ")
    print(f"la memoria ram es {ram} GB")
    almacenamiento = pedir_entero("Ingresa el almacenamiento del equipo: ")
    print(f"El almacenamiento es de {almacenamiento} GB")
    sistema_operativo = input("Ingrese el sistema operativo del Equipo: ")
    tiene_fallas = pedir_bool("El Equipo tiene alguna falla:  ")
    estado = input("En que estado se encuentra el equipo: ")
    valor_costo = pedir_float("Ingresa el precio del equipo: ")
    valor_comercializacion = pedir_float("ingresa el valor en el que se puede revender este equipo: ")
    diferencia = valor_costo - valor_comercializacion
    print(f"La diferencia del es: {diferencia}")
    color = input("Ingresa el color del equipo: ")

    
    
    equipo = {
    "numero_inventario" : numero_inventario,
    "numero_activo" : numero_activo,
    "area" : area,
    "persona_a_cargo" : persona_a_cargo,
    "usuario" : usuario,
    "nombre_equipo" : nombre_equipo,
    "numero_serie" : numero_serie,
    "marca" : marca,
    "modelo_comercial" : modelo_comercial,
    "modelo_fabricante" : modelo_fabricante,
    "imei" : imei,
    "procesador" : procesador,
    "ram" : ram,
    "almacenamiento" : almacenamiento,
    "sistema_operativo" : sistema_operativo,
    "tiene_fallas" : tiene_fallas,
    "estado" : estado,
    "valor_costo" : valor_costo,
    "valor_comercializacion" : valor_comercializacion,
    "diferencia" : diferencia,
    "color" : color

}

    equipos.append(equipo)
    print("Equipo agregado correctamente")

def mostrar_equipo():
    if not equipos:
        print("no hay equipos registrados")
        return
    
    
    for equipo in equipos:
        print(equipo)

def buscar_marca():
    if not equipos:
        print("no hay equipos registrados")
        return
    
    buscar_marca = input("Ingrese la Marca del equipo: ").lower()
    

    for equipo in equipos:
        if equipo["marca"].lower() == buscar_marca:
            print(equipo) 



def mostrar_menu():
    while True:

        print("==BIENVENIDO==")
        print("1.Ingresa el Equipo")
        print("2.Mostrar Equipo")
        print("3.Buscar por marca")
        print("4.Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            agregar_equipo()
        elif opcion == "2":
            mostrar_equipo()
        elif opcion == "3":
            buscar_marca()
        elif opcion == "4":
            print("Saliendo del programa")
            break   
        else:
            print("Opcion invalida")



mostrar_menu()






    




