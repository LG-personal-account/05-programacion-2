# ENUNCIADO 12
# Dada una lista de palabras, obtené el set de las que empiezan con vocal.


palabras = ["mesa", "árbol", "sol", "escuela", "isla", "banana", "uva"]
con_vocal = {p for p in palabras if p[0].lower() in "aeiouáéíóú"}
print(con_vocal)
