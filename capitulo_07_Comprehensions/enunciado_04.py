# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# ENUNCIADO 4
# Dada la lista list(range(1, 21)), generar una lista con los
# números divisibles por 3 o por 5.
# -----------------------------------------------------------------------------

# Colección destino = [expresión - ¿Qué hago con los datos? - for elemento in
# colección - ¿De dónde saco los datos? - ¿Que datos quiero?]
# [todo numero en rango 1 a 20 que sea divisible por 5 o 3]
divisibles = [n for n in range(1, 21) if n % 3 == 0 or n % 5 == 0]
print(divisibles)
