# ENUNCIADO 17
# Con el mismo diccionario del ejercicio 16, calculá el valor total del inventario (precio × stock, sumados) usando una comprensión generadora dentro de sum().


catalogo = {
    "pan": {"precio": 500, "stock": 20},
    "leche": {"precio": 800, "stock": 5},
    "queso": {"precio": 1200, "stock": 0},
    "yerba": {"precio": 3500, "stock": 15}
}

total = sum(datos["precio"] * datos["stock"] for datos in catalogo.values())
print(f"Valor total del inventario: ${total}")
