# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# ENUNCIADO 10
# Invertí este diccionario: {"a": 1, "b": 2, "c": 3}
# -> {1: "a", 2: "b", 3: "c"}.
# -----------------------------------------------------------------------------


original = {"a": 1, "b": 2, "c": 3}

# Colección destino = [expresión - ¿Qué hago con los datos? - for elemento in
# colección - ¿De dónde saco los datos? - ¿Que datos quiero?]
# Repasando diccionario: original.items() devuelve una lista de tuplas
# [(clave, valor), (clave, valor), ...]
# Otras funciones usadas son original.keys() que devuelve una lista de claves y
# original.values() que devuelve una lista de valores.
# Aquí {armo valor:clave, buscando por cada clave en original usando .items()
# para recibir cada tupla (clave, valor)}
invertido = {v: k for k, v in original.items()}
print(invertido)
