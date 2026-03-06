num1 = int(input("Ingresa un Numero: "))
num2 = int(input("Ingrese un Numero: "))

operacion = input("Elija la Operacion que deseas Realizar(+, -, *, /)")

if operacion == "+":
    print(f"La Resultado es: {num1 + num2}")
elif operacion == "-":
    print(f"El Resultado es: {num1 - num2}")
elif operacion == "*":
    print(f"El Resultado es: {num1 * num2}")
elif operacion == "/":
    print(f"El Resultado es: {num1 / num2}")
    