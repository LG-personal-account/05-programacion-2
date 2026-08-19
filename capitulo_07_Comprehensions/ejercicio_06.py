# Ejercicio 6
# Dada la frase "el perro y el gato y el perro", obtener el set de palabras únicas.

frase = "el perro y el gato y el perro"
unicas = {palabra for palabra in frase.split()}
print(unicas)
