# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# ENUNCIADO 5
# Dado un string, generar una lista con las posiciones en las
# que aparece la letra "a" (usá enumerate()).
# -----------------------------------------------------------------------------


texto = input("Texto: ")

# Colección destino = [expresión - ¿Qué hago con los datos? - for elemento in
# colección - ¿De dónde saco los datos? - ¿Que datos quiero?]
# [Para encontrar los lugares que aparece la letra a, pedimos:}
# toda posición por indice de letra in un texto enumerado y
# pasado a minúscula de letra que coincida con la pedida]
posiciones = [i for i, letra in enumerate(texto.lower()) if letra == "a"]
print(f"La 'a' aparece en las posiciones: {posiciones}")
