def num_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor         
        except ValueError:
            print("Ingrese el tipo de valor correcto")


num1 = num_entero("Ingresa un numero: ")
num2 = num_entero("Ingresa un numero: ")

def operacion():
    while True:
        print("Selecciona el tipo de operacion que deseas realizar: (+, -, *, /) ")

        opcion = input("Selecciona una opercaion: ")

        if opcion == "+":
            print(num1 + num2)
        elif opcion == "-":
            print(num1 - num2)
        elif opcion == "*":
            print(num1 * num2)
        elif  opcion == "/":
                if num2 == 0:
                    print("No se puede dividir entre cero")
                    continue
                print(num1 / num2)
        break
        

operacion()
