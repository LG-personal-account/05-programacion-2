# Ejercicio 4
# Dada una frase ingresada por el usuario, generá una lista con solo las letras (sin espacios ni signos).

frase = input("Frase: ")
letras = [c for c in frase if c.isalpha()]
print(letras)
print(f"Hay {len(letras)} letras en total")
