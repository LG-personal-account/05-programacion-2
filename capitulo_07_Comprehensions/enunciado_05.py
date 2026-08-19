# ENUNCIADO 5
# Dado un string, generá una lista con las posiciones en las que aparece la letra "a" (usá enumerate()).


texto = input("Texto: ")
posiciones = [i for i, letra in enumerate(texto.lower()) if letra == "a"]
print(f"La 'a' aparece en las posiciones: {posiciones}")
