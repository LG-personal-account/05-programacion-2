# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# ENUNCIADO 13
# Dada la lista [7, 3, 3, 5, 9, 7, 2, 5, 9, 9], obtené el set
# de los números que se repiten (aparecen más de una vez).
# Pista: podés usar .count().
# -----------------------------------------------------------------------------


numeros = [7, 3, 3, 5, 9, 7, 2, 5, 9, 9]

# Colección destino = [expresión - ¿Qué hago con los datos? - for elemento in
# colección - ¿De dónde saco los datos? - ¿Que datos quiero?]
# Colección destino (repetidos) = [¿Qué hago con los datos? se guardan como
# vienen - for elemento in colección - ¿De dónde saco los datos? - ¿Que datos quiero?]
repetidos = {n for n in numeros if numeros.count(n) > 1}
print(repetidos)
