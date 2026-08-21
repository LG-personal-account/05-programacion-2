# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# ENUNCIADO 9
# Dado un texto, generar un diccionario {palabra: longitud} con cada
# palabra única y su cantidad de letras.
# -----------------------------------------------------------------------------


texto = input("Texto: ")

# Colección destino = [expresión - ¿Qué hago con los datos? - for elemento in
# colección - ¿De dónde saco los datos? - ¿Que datos quiero?]
# [todo palabra en texto acompañado de su longitud]
longitudes = {palabra: len(palabra) for palabra in set(texto.lower().split())}
print(longitudes)
