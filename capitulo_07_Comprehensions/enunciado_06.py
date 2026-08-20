# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# ENUNCIADO 6
# Dada la lista [15, 22, 8, 34, 7, 41, 19], generá una lista donde
# cada número esté acompañado por su clasificación:
# [(15, "impar"), (22, "par"), (8, "par"), ...]. Usá una expresión
# condicional ("par" if n % 2 == 0 else "impar").
# -----------------------------------------------------------------------------


numeros = [15, 22, 8, 34, 7, 41, 19]
clasificados = [(n, "par" if n % 2 == 0 else "impar") for n in numeros]
print(clasificados)
