from paquete.utils import pedir_int

            

def calculadora():
    while True:
        num1 = pedir_int("Ingresa un numero: ")
        num2 = pedir_int("Ingresa un numero: ")

        operacion = input("Operacion: (Suma), (Resta), (Multiplicacion), (Division): ").lower()
        if operacion == "suma":
            print(f"El Resultado es: {num1 + num2}")
        elif operacion == "resta":
            print(f"El Resultado es: {num1 - num2}")
        elif operacion == "multiplicacion":
            print(f"El Resultado es: {num1 * num2}")
        elif operacion == "division":
            print(f"El resultado es: {num1 / num2}")
            



