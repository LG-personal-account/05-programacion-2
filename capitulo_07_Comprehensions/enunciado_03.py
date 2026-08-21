# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# ENUNCIADO 3
# Convertí la lista ["hola", "mundo", "python"] a una lista con
# todas las palabras en mayúsculas.
# -----------------------------------------------------------------------------


palabras = ["hola", "mundo", "python"]

# Colección destino = [expresión - ¿Qué hago con los datos? - for elemento in
# colección - ¿De dónde saco los datos?]
# [pasar a mayúscula toda palabra en palabras]
mayus = [p.upper() for p in palabras]
print(mayus)
