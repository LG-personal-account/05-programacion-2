# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# ENUNCIADO 8
# Dado el diccionario {"pan": 500, "leche": 800, "queso": 1200,
# "yerba": 3000}, generar un diccionario nuevo con los precios en
# dólares (dividir por 1000 y redondear a 2 decimales).
# -----------------------------------------------------------------------------


precios = {"pan": 500, "leche": 800, "queso": 1200, "yerba": 3000}

# Colección destino = {expresión - ¿Qué hago con los datos? - for elemento in
# colección - ¿De dónde saco los datos? - ¿Que datos quiero?}
# creo la colección en_dolares = {¿Que hago con los datos?
# armo una clave producto: y un valor (precio en dolares con 2 decimales) -
# ¿Que recibo? una tupla (producto, precio) cuyos elementos guardo en producto
# y precio - ¿De dónde saco los datos? precios.items() de la colección precios}
en_dolares = {
    producto: round(precio / 1000, 2)
    for producto, precio in precios.items()
}
print(en_dolares)
