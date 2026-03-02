suma = "resultado"

num1 =int(input("ingresa un numero: "))
num2 =int(input("ingresa otro numero por Favor: "))

operacion = (input("Ingrese la operecion que quieras hacer (+ * - /)  "))

if operacion == "+":
    print(f"la suma es: {num1 + num2} ")
elif operacion == "*":
    print (f"la  multiplicacion es: {num1 * num2}")
elif operacion == "-":
    print(f"La resta es: {num1 - num2}")
elif operacion == "/":
    print(f"La division es: {num1 / num2}")
else:
    print("ingresa una Operacion Valida")




