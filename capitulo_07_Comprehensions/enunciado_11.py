# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# ENUNCIADO 11
# Dado el diccionario {"Ana": 8, "Juan": 5, "Pedro": 9,
# "Lucía": 4, "Diego": 7}, generá otro diccionario que
# contenga solo los aprobados (nota >= 7).
# -----------------------------------------------------------------------------


notas = {"Ana": 8, "Juan": 5, "Pedro": 9, "Lucía": 4, "Diego": 7}
aprobados = {nombre: nota for nombre, nota in notas.items() if nota >= 7}
print(aprobados)
