def pedir_entero(mensaje):
        while True:
            try:
                return int(input(mensaje))
            except ValueError:
                print(" Debes ingresar un número válido") 

def pedir_bool(mensaje):
        while True:
            valor = input(mensaje + " (Si/No): ").strip().lower()
            if valor == "si":
                return True 
            elif valor == "no":
                return False
            else:
                print(" Debes ingresar Si o No")
