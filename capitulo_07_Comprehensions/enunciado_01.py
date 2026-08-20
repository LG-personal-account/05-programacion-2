# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# ENUNCIADO 1
# Generar una lista con los primeros 20 múltiplos de 5
# (5, 10, 15, ..., 100).
# -----------------------------------------------------------------------------

# [expresión for elemento in colección]
# [multiplicar por 5 todo numero en rango 1 a 20]
multiplos = [n * 5 for n in range(1, 21)]
print(multiplos)
