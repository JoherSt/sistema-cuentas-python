def pedir_int(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Por favor Ingresa el Tipo de Dato Correspondiente")