# Ejercicio 2
# Una calculadora simple que pida dos números y una operación (+, -, *, /), y muestre el resultado. Debe manejar entradas no numéricas y división por cero, con mensajes distintos.

try:
    a = float(input("Primer número: "))
    b = float(input("Segundo número: "))
    op = input("Operación (+, -, *, /): ")
    if op == "+":
        print(a + b)
    elif op == "-":
        print(a - b)
    elif op == "*":
        print(a * b)
    elif op == "/":
        print(a / b)
    else:
        print("Operación no reconocida")
except ValueError:
    print("Los números deben ser válidos")
except ZeroDivisionError:
    print("No se puede dividir por cero")
