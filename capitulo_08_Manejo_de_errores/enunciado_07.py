# ENUNCIADO 7
# Un programa que insista al usuario hasta que ingrese un número válido: usá un while True y un break dentro del else del try.


while True:
    try:
        numero = int(input("Número: "))
    except ValueError:
        print("Eso no es un número, probá de nuevo")
    else:
        break


print(f"Perfecto, ingresaste {numero}")
