# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# ENUNCIADO 2
# Dada la lista [3, 8, -2, 7, -5, 0, 12, -4], generar una lista con
# los valores absolutos (usá abs()).
# -----------------------------------------------------------------------------

numeros = [3, 8, -2, 7, -5, 0, 12, -4]

# [expresión for elemento in colección]
# [valor absoluto de cada numero en numeros]
absolutos = [abs(n) for n in numeros]
print(absolutos)
