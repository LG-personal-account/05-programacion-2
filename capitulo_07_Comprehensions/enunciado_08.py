# ENUNCIADO 8
# Dado el diccionario {"pan": 500, "leche": 800, "queso": 1200, "yerba": 3000}, generá un diccionario nuevo con los precios en dólares (dividir por 1000 y redondear a 2 decimales).


precios = {"pan": 500, "leche": 800, "queso": 1200, "yerba": 3000}
en_dolares = {producto: round(precio / 1000, 2) for producto, precio in precios.items()}
print(en_dolares)
