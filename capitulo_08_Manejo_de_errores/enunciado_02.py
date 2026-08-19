# ENUNCIADO 2
# Pedile dos números y mostrar la división. Manejar por separado el caso de entrada no numérica y el de división por cero.


try:
    a = float(input("Numerador: "))
    b = float(input("Denominador: "))
    print(f"Resultado: {a / b}")
except ValueError:
    print("Los números deben ser válidos")
except ZeroDivisionError:
    print("No se puede dividir por cero")
