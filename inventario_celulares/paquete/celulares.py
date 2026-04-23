
from .utils import pedir_bool, pedir_entero, pedir_float
from .datos import celulares



def agregar_celular():
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

    
    
    celular = {
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

    celulares.append(celular)
    print("Equipo agregado correctamente")

def mostrar_celular():
    if not celulares:
        print("no hay equipos registrados")
        return
    
    
    for celular in celulares:
        print(celular)

def buscar_marca():
    if not celulares:
        print("no hay equipos registrados")
        return
    
    buscar_marca = input("Ingrese la Marca del equipo: ").lower()
    

    for celular in celulares:
        if celular["marca"].lower() == buscar_marca:
            print(celular) 









    




