# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# ENUNCIADO 16
# Dado el diccionario {"pan": {"precio": 500, "stock": 20},
# "leche": {"precio": 800, "stock": 5},
# "queso": {"precio": 1200, "stock": 0},
# "yerba": {"precio": 3500, "stock": 15}}, obtené una lista
# con los nombres de los productos con stock disponible.
# -----------------------------------------------------------------------------


catalogo = {
    "pan": {"precio": 500, "stock": 20},
    "leche": {"precio": 800, "stock": 5},
    "queso": {"precio": 1200, "stock": 0},
    "yerba": {"precio": 3500, "stock": 15}
}

disponibles = [
    producto
    for producto, datos in catalogo.items()
    if datos["stock"] > 0
]
print(disponibles)
