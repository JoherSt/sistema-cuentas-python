num1 = int(input("Ingresa un numero: "))
num2 = int(input("Ingresa un numero: "))

operacion = input("elije una opcion (+ - * / :  )")

if operacion == "+":
    print(f"El resultado de la Suma es: {num1 + num2}")
elif operacion == "-":
    print(f"El resultado de la Resta en: {num1 - num2}")
elif operacion == "*":
    print(f"La Resultado de la Multiplicacion es:{num1 * num2}")
elif operacion == "/":
    print(f"El Resultado de la Division es: {num1 / num2}")



