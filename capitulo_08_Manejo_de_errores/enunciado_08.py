# ENUNCIADO 8
# Función abrir_configuracion(nombre_archivo) que intente abrir un archivo, y si no existe devolver el contenido, o un string vacío si no existe. Manejar FileNotFoundError. (Podés simularlo llamando la función con un nombre inventado.)


def abrir_configuracion(nombre_archivo):
    try:
        with open(nombre_archivo) as f:
            return f.read()
    except FileNotFoundError:
        return {}


config = abrir_configuracion("no_existe.txt")
print(config)
