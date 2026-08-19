# Ejercicio 3
# Convertí un pedido de edad en un bloque completo: el try intenta convertir, el except ValueError maneja el error, el else felicita al usuario, y el finally imprime "Gracias por participar" siempre.

try:
    edad = int(input("Edad: "))
except ValueError:
    print("No ingresaste un número válido")
else:
    print(f"Perfecto, tenés {edad} años")
finally:
    print("Gracias por participar")
