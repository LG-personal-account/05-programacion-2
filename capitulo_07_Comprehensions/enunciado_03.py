# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# ENUNCIADO 3
# Convertí la lista ["hola", "mundo", "python"] a una lista con
# todas las palabras en mayúsculas.
# -----------------------------------------------------------------------------


palabras = ["hola", "mundo", "python"]

# [expresión for elemento in colección]
# [pasar a mayúscula toda palabra en palabras]
mayus = [p.upper() for p in palabras]
print(mayus)
