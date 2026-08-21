# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# ENUNCIADO 6
# Dada la lista [15, 22, 8, 34, 7, 41, 19], generar una lista donde
# cada número esté acompañado por su clasificación:
# [(15, "impar"), (22, "par"), (8, "par"), ...]. Usá una expresión
# condicional ("par" if n % 2 == 0 else "impar").
# -----------------------------------------------------------------------------


numeros = [15, 22, 8, 34, 7, 41, 19]

# Colección destino = [expresión - ¿Qué hago con los datos? - for elemento in
# colección - ¿De dónde saco los datos?]
# [todo numero en numeros acompañado de su clasificación par/impar]
clasificados = [(n, "par" if n % 2 == 0 else "impar") for n in numeros]
print(clasificados)
