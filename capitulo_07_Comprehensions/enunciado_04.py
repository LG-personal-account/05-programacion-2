# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# ENUNCIADO 4
# Dada la lista list(range(1, 21)), generar una lista con los
# números divisibles por 3 o por 5.
# -----------------------------------------------------------------------------

# [expresión for elemento in colección]
# [todo numero en rango 1 a 20 que sea divisible por 5 o 3]
divisibles = [n for n in range(1, 21) if n % 3 == 0 or n % 5 == 0]
print(divisibles)
