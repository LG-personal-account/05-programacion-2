# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# ENUNCIADO 11
# Dado el diccionario {"Ana": 8, "Juan": 5, "Pedro": 9,
# "Lucía": 4, "Diego": 7}, generar otro diccionario que
# contenga solo los aprobados (nota >= 7).
# -----------------------------------------------------------------------------


notas = {"Ana": 8, "Juan": 5, "Pedro": 9, "Lucía": 4, "Diego": 7}


# Colección destino = [expresión - ¿Qué hago con los datos? - for elemento in
# colección - ¿De dónde saco los datos? - ¿Que datos quiero?]
# [todo nombre en nombres acompañado de su nota en notas, usando zip()]
aprobados = {nombre: nota for nombre, nota in notas.items() if nota >= 7}
print(aprobados)
