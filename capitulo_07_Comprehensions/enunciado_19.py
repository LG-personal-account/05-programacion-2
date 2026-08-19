# ENUNCIADO 19
# Con la misma matriz, obtené una lista solo con los números pares.


matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
pares = [x for fila in matriz for x in fila if x % 2 == 0]
print(pares)
