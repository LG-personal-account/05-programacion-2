# ENUNCIADO 15
# Función parsear_fecha(texto) que reciba una fecha tipo "25/07/2026" y devuelva una tupla (día, mes, año) con enteros. Si el formato es inválido, lanzá ValueError con mensaje claro.


def parsear_fecha(texto):
    try:
        partes = texto.split("/")

        if len(partes) != 3:
            raise ValueError("Formato inválido, se esperaba dd/mm/aaaa")

        dia = int(partes[0])
        mes = int(partes[1])
        año = int(partes[2])

        return dia, mes, año

    except ValueError as e:
        raise ValueError(f"No se pudo parsear '{texto}': {e}")


try:
    print(parsear_fecha("25/07/2026"))
    print(parsear_fecha("25-07-2026"))
except ValueError as e:
    print(e)
