# ENUNCIADO 12
# Una calculadora de raíz cuadrada. Usá math.sqrt() (importalo). Manejar entrada no numérica y números negativos con mensajes distintos.


from math import sqrt


try:
    numero = float(input("Número: "))

    if numero < 0:
        print("No se puede calcular la raíz de un número negativo")
    else:
        print(f"√{numero} = {sqrt(numero):.4f}")

except ValueError:
    print("Ingresá un número válido")
