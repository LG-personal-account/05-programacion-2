# ENUNCIADO 14
# Simulá un cajero automático: pedí el saldo actual y el monto a extraer. Si el monto es mayor al saldo, lanzá una excepción ValueError con mensaje "Saldo insuficiente". Manejala.


try:
    saldo = float(input("Saldo actual: "))
    monto = float(input("Monto a extraer: "))

    if monto > saldo:
        raise ValueError("Saldo insuficiente")

    saldo -= monto
    print(f"Extracción exitosa. Nuevo saldo: ${saldo:.2f}")

except ValueError as e:
    print(f"Error: {e}")
