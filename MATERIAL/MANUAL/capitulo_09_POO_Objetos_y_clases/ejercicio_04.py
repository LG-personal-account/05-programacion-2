# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# Ejercicio 4
# Ampliá la clase Producto(nombre, precio) agregándole stock (que arranca
# en 0). Sumale dos métodos: reponer(cantidad) que aumenta el stock, y
# valor_stock() que devuelve precio * stock. Uno modifica, el otro solo
# consulta.
# -------------------------------------------------------------------------

class Producto:

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        self.stock = 0

    def reponer(self, cantidad):
        self.stock += cantidad

    def valor_stock(self):
        return self.precio * self.stock

yerba = Producto("Yerba", 3500)

yerba.reponer(20)

print(f"Stock: {yerba.stock}")
print(f"Valor: ${yerba.valor_stock()}")
