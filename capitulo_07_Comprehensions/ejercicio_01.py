# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Ejercicio 1
# Escribí una comprensión que genere una lista con los números
# del 1 al 10 multiplicados por 3.
# -----------------------------------------------------------------------------

# [expresion for elemento in colección]
# [multiplicar por 3 todo n de lista del rango 1 al 10]
triples = [n * 3 for n in range(1, 11)]
print(triples)
