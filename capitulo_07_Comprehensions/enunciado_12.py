# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# ENUNCIADO 12
# Dada una lista de palabras, obtené el set de las que empiezan
# con vocal.
# -----------------------------------------------------------------------------

# Colección destino = [expresión - ¿Qué hago con los datos? - for elemento in
# colección - ¿De dónde saco los datos? - ¿Que datos quiero?]
# Colección destino (con_vocal) = [¿Qué hago con los datos?, nada - for
# elemento (p) in colección (palabras) - Las palabras cuya primera letra (p[0])
# esté en el conjunto de vocales (aeiouáéíóú)]
palabras = ["mesa", "árbol", "sol", "escuela", "isla", "banana", "uva"]
con_vocal = {p for p in palabras if p[0].lower() in "aeiouáéíóú"}
print(con_vocal)
