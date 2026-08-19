# ENUNCIADO 20
# Dado un diccionario de alumnos con notas por materia, generá un diccionario {nombre: promedio} usando comprensión de diccionario.


alumnos = {
    "Ana": {"Matemática": 8, "Programación": 9, "Física": 7},
    "Juan": {"Matemática": 6, "Programación": 8, "Física": 5},
    "Pedro": {"Matemática": 10, "Programación": 7, "Física": 9}
}

promedios = {
    nombre: sum(materias.values()) / len(materias)
    for nombre, materias in alumnos.items()
}

for nombre, promedio in promedios.items():
    print(f"{nombre}: {promedio:.2f}")
