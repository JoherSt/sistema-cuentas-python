equipos = []

def pedir_entero (mensaje):
    while True:
        try:
             return int(input(mensaje)) 
        except ValueError:
            print("por favor Ingresa un numero valido")
            
def pedir_bool (mensaje):
    while True:
        valor = input(mensaje + "(Si/No)").lower().strip()
        if valor  ==   "si":
                return True
        elif valor == "no":
                return False
        else:
            print("Ingresa el tipo de valor que se te esta pidiendo: ")
def agregar_equipo():
     print("==INGRESANDO NUEVO EQUIOPO==")
     numero_inventario = pedir_entero("Ingresa el N°Inventario: ")
     numero_activo = pedir_entero("Ingresa el N°Activo: ")
     area = input("Ingrese la Area a la que pertenece: ")
     persona_a_cargo = input("Ingresa el Nombre de la Persona a cargo de este equipo: ")
     usuario = input("Ingresa el Nombre del Usuario de este Equipo:")
     contraseña = input ("Ingresa la contraseña: ")
     marca = input("Ingresa la Marca: ")
     modelo = input("Ingresa el modelo: ")
     numero_serie = input("Ingresa el numero de Serie:")
     modo_bios = input("Ingresa el modo de bios: ")
     serie_bios = input("Ingresa la Serie de Bios: ")
     procesador = input("Ingresa la Memoria RAM: ")
     almacenamiento = input("Ingrese el almacenamiento: ")
     sitema_operativo = input("Ingresa el Sistema Operativo: ")
     estado = input("Ingresa el estado en el que se enecuetra el Equipo: ")
     anotaciones = input("Ingresa si el Equipo tiene Alguna falla:") 
     valor_costo = pedir_entero("Ingresa el valor del equipo: ")
     valor_comercializacion = pedir_entero("Ingresa el valor de Comercializacion de este equipo: ")
     diferencia = valor_costo - valor_comercializacion 
     print(f"La diferencia de precios es: {diferencia}")
     licencia_office = pedir_bool("Su equipo cuenta con licencia Office(Si/No): ") 
     licencia_windows = pedir_bool("Su equipo Cuenta con licencia Windows(Si/No)")


     equipo = {
          "numero de inventario" : numero_inventario,
          "numero de activo" : numero_activo,
          "area" : area,
          "persona a cargo" : persona_a_cargo,
          "usuario" : usuario,
          "contraseña" : contraseña,
          "Marca" : marca,
          "modelo" : modelo,
          "Numero de serie" : numero_serie,
          "Modo de bios" : modo_bios,
          "Serie de bios" : serie_bios,
          "procesador" : procesador,
          "almacenamiento" : almacenamiento,
          "sisteama operativo" : sitema_operativo,
          "estado" : estado,
          "anotaciones" : anotaciones,
          "valor costo" : valor_costo,
          "valor comercializacion" : valor_comercializacion,
          "diferencia" : diferencia,
          "licencia office" : licencia_office,
          "licencia_windows" : licencia_windows


         
 
     }
     equipos.append(equipo)
     print("Se agrego correctamente el Equipo")

agregar_equipo()


def mostrar_equipos():
    if not equipos:
        print(" No hay equipos registrados ")
        return

    print(" LISTA DE EQUIPOS ") 
    for equipo in equipos:
        for clave, valor in equipo.items():
            print(f"{clave}: {valor}")
        print()









