# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# ENUNCIADO 18
# Dada la matriz [[1, 2, 3], [4, 5, 6], [7, 8, 9]], obtené una
# lista aplanada con todos los elementos. Se permite comprensión
# anidada.
# -----------------------------------------------------------------------------


matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
aplanada = [x for fila in matriz for x in fila]
print(aplanada)
