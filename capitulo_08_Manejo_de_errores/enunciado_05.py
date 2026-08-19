# ENUNCIADO 5
# Un menú con opciones 1 a 4. Si el usuario ingresa algo que no es un número, mostrar "Ingresá un número". Si es un número fuera de rango, mostrar "Opción inexistente".


try:
    opcion = int(input("Opción (1-4): "))
    if opcion < 1 or opcion > 4:
        print("Opción inexistente")
    else:
        print(f"Elegiste la opción {opcion}")
except ValueError:
    print("Ingresá un número")
