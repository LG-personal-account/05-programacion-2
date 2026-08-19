# ENUNCIADO 14
# Dada la lista de precios [500, 1200, 800, 1500, 950, 2000, 3500], calculá con una comprensión generadora dentro de sum() la suma total, y el promedio.


precios = [500, 1200, 800, 1500, 950, 2000, 3500]

total = sum(p for p in precios)
promedio = sum(p for p in precios) / len(precios)

print(f"Total: ${total}")
print(f"Promedio: ${promedio:.2f}")
