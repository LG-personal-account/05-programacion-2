# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Ejercicio 4
# Dada una frase ingresada por el usuario, generar una lista con solo
# las letras (sin espacios ni signos).
# -----------------------------------------------------------------------------


frase = input("Frase: ")

# [expresión for elemento in colección]
# [todo caracter de caracteres en frase si caracter es una letra]
letras = [c for c in frase if c.isalpha()]
print(letras)
print(f"Hay {len(letras)} letras en total")
