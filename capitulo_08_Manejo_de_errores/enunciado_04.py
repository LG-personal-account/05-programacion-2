# ENUNCIADO 4
# Pedí una edad. Si es un número negativo o mayor a 130, lanzá una ValueError con un mensaje claro. Atrapala y mostrá el error.


try:
    edad = int(input("Edad: "))
    if edad < 0 or edad > 130:
        raise ValueError(f"Edad fuera de rango: {edad}")
    print(f"Tu edad es {edad}")
except ValueError as e:
    print(f"Error: {e}")
