# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Ejercicio 5
# Dada la lista ["Ana", "Juan", "Pedro", "Lucía"], genera un
# diccionario donde la clave sea el nombre y el valor su longitud.
# -----------------------------------------------------------------------------

nombres = ["Ana", "Juan", "Pedro", "Lucía"]

# [expresión for elemento in colección]
# Es un diccionario con clave:valor, donde la clave es el nombre y el valor
# es la longitud del nombre. Por eso usamos llaves {} en lugar de corchetes [].
# [por cada nombre guarda, nombre:largo por cada nombre de nombres]
longitudes = {n: len(n) for n in nombres}
print(longitudes)
