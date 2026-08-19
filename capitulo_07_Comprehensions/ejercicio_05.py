# Ejercicio 5
# Dada la lista ["Ana", "Juan", "Pedro", "Lucía"], generá un diccionario donde la clave sea el nombre y el valor su longitud.

nombres = ["Ana", "Juan", "Pedro", "Lucía"]
longitudes = {n: len(n) for n in nombres}
print(longitudes)
