# ENUNCIADO 13
# Función elemento_seguro(lista, indice) que devuelva el elemento de la lista en esa posición, o None si el índice está fuera de rango. Usá try/except IndexError.


def elemento_seguro(lista, indice):
    try:
        return lista[indice]
    except IndexError:
        return None


nums = [10, 20, 30]

print(elemento_seguro(nums, 1))
print(elemento_seguro(nums, 100))
