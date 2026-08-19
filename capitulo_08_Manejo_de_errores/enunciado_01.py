# ENUNCIADO 1
# Pedile al usuario un número entero. Si ingresa cualquier otra cosa, mostrar "Entrada inválida" y no cortar el programa.


try:
    numero = int(input("Número entero: "))
    print(f"Ingresaste {numero}")
except ValueError:
    print("Entrada inválida")
