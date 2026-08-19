# ENUNCIADO 7
# Dada la lista de nombres ["Ana", "Juan", "Sofía", "Pedro", "Lucía"] y la lista de notas [8, 6, 9, 5, 7], generá una lista de strings tipo "Ana: 8" usando zip().


nombres = ["Ana", "Juan", "Sofía", "Pedro", "Lucía"]
notas = [8, 6, 9, 5, 7]
reporte = [f"{n}: {nota}" for n, nota in zip(nombres, notas)]
print(reporte)
