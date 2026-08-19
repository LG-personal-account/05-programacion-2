# Ejercicio 1
# Reescribí este código para que use try/except en vez de isdigit(). Debe aceptar negativos.

entrada = input("Número: ")
try:
    numero = int(entrada)
    print(f"El doble es {numero * 2}")
except ValueError:
    print("No es un número")
