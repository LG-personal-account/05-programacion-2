# ENUNCIADO 4
# Dada la lista list(range(1, 21)), generá una lista con los números divisibles por 3 o por 5.


divisibles = [n for n in range(1, 21) if n % 3 == 0 or n % 5 == 0]
print(divisibles)
