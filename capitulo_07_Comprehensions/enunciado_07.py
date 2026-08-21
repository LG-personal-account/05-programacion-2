# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# ENUNCIADO 7
# Dada la lista de nombres ["Ana", "Juan", "Sofía", "Pedro",
# "Lucía"] y la lista de notas [8, 6, 9, 5, 7], generar una
# lista de strings tipo "Ana: 8" usando zip().
# -----------------------------------------------------------------------------


nombres = ["Ana", "Juan", "Sofía", "Pedro", "Lucía"]
notas = [8, 6, 9, 5, 7]

# Colección destino = [expresión - ¿Qué hago con los datos? - for elemento in
# colección - ¿De dónde saco los datos? - ¿Que datos quiero?]
# [todo nombre en nombres acompañado de su nota en notas, usando zip()]
reporte = [f"{n}: {nota}" for n, nota in zip(nombres, notas)]
print(reporte)
