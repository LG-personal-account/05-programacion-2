# Ejercicio 4
# Escribí una función calcular_imc(peso, altura) que lance ValueError si el peso o la altura son menores o iguales a cero. Luego atrapá la excepción y mostrá el mensaje de error.

def calcular_imc(peso, altura):
    if peso <= 0 or altura <= 0:
        raise ValueError("Peso y altura deben ser positivos")
    return peso / (altura ** 2)

try:
    imc = calcular_imc(70, -1.75)
except ValueError as e:
    print(f"Error: {e}")
