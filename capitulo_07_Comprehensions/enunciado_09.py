# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# ENUNCIADO 9
# Dado un texto, generá un diccionario {palabra: longitud} con cada
# palabra única y su cantidad de letras.
# -----------------------------------------------------------------------------


texto = input("Texto: ")
longitudes = {palabra: len(palabra) for palabra in set(texto.lower().split())}
print(longitudes)
