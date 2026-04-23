def pedir_entero(mensaje):
    while True:
        try: 
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Por favor Ingresa un valor valido")

def pedir_float(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            return valor
        except ValueError:
            print("Por favor ingresa un valor valido: ")