# ENUNCIADO 11
# Pedí un año de nacimiento. Calculá la edad. Manejar entrada no numérica y también años futuros o menores a 1900 (lanzá ValueError en esos casos).


from datetime import datetime


try:
    año = int(input("Año de nacimiento: "))
    año_actual = datetime.now().year

    if año > año_actual:
        raise ValueError("No podés haber nacido en el futuro")

    if año < 1900:
        raise ValueError("Año demasiado antiguo")

    edad = año_actual - año
    print(f"Tenés {edad} años")

except ValueError as e:
    print(f"Error: {e}")
