from .utils import pedir_entero, pedir_float
from .datos import equipos


def agregar_producto():
    nombre = input("Ingresa tu Nombre: ")
    codigo = input("Ingresa el Codigo: ")
    precio = pedir_float("Ingresa el precio: ")
    stok = pedir_entero("Ingrese la cantidad de Equipos disponibles: ")
    ventas = pedir_float("Ingresa la Cantidad de equipos vendidos: ")

    equipo = {
        "nombre" : nombre,
        "codigo" : codigo,
        "precio" : precio,
        "stok" : stok,
        "ventas" : ventas
    }

    equipos.append(equipo)
    print("Equipo agregado Exitosamente")

def mostrar_producto():
    if not equipos:
        print("No hay Ningun producto registrado: ")
        return
    
    for equipo in equipos:
        print("Equipo Encontrado")
        print(f"nombre {equipo['nombre']}")
        print(f"codigo {equipo['codigo']}")
        print(f"precio {equipo['precio']}")
        print(f"stok {equipo['stok']}")
        print(f"ventas {equipo['ventas']}")


def buscar_producto():
    if not equipos:
        print("No hay ningun equipo registrado")
        return
    
    codigo = input("Ingresa el codigo del equipo: ")

    for equipo in equipos:
        if equipo["codigo"] == codigo:
            print("Equipo Encontrado")
            print(equipo)
            return
    
    print("No se ha encontrado ningun dato")

def vender_producto():
    if not equipos:
        print("No hay productos registrados")
        return

    codigo = input("Ingresa el codigo del producto: ")

    for equipo in equipos:
        if equipo["codigo"] == codigo:
            print(f"Producto encontrado: {equipo['nombre']}")
            print(f"Stock disponible: {equipo['stok']}")

            cantidad = pedir_entero("¿Cuantas unidades deseas vender?: ")

            if cantidad <= 0:
                print("Cantidad invalida")
                return

            if cantidad > equipo["stok"]:
                print("No hay suficiente stock")
                return

            equipo["stok"] -= cantidad
            equipo["ventas"] += cantidad

            total = equipo["precio"] * cantidad

            print("Venta realizada con exito")
            print(f"Total a pagar: {total}")

            return

    print("No se encontro el producto")

def editar_producto():
    if not equipos:
        print("No hay equipos registrados")
        return
    
    codigo = input("Ingresa el codigo del equipo que quires editar: ")

    for equipo in equipos:
        if equipo["codigo"] == codigo :
            print("Equipo Encontrado")
            print(f"nombre {equipo['nombre']}")
            print(f"codigo {equipo['codigo']}")
            print(f"precio {equipo['precio']}")
            print(f"stok {equipo['stok']}")
            print(f"ventas {equipo['ventas']}")

            equipo["nombre"] = input("Ingresa el nuevo nombre: ")
            equipo["codigo"] = input("Ingresa el nuevo codigo: ")
            equipo["precio"] = input("Ingresa el nuevo precio: ")
            equipo["stok"] = input("Ingresa el nuevo stok: ")
            equipo["ventas"] = input("Ingresa la nueva venta: ")
        
        print("Equipo agregado correctamente")






    


