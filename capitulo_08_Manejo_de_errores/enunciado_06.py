# ENUNCIADO 6
# Función promedio_seguro(lista) que calcule el promedio de una lista de números, pero devuelva 0 si la lista está vacía. Usá try/except ZeroDivisionError.


def promedio_seguro(lista):
    try:
        return sum(lista) / len(lista)
    except ZeroDivisionError:
        return 0


print(promedio_seguro([7, 8, 9]))
print(promedio_seguro([]))
