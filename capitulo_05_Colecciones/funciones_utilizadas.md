# Funciones Utilizadas en Colecciones

Documento que agrupa todas las funciones (built-in y métodos) utilizadas en los ejercicios y enunciados, organizadas por tipo de dato y en orden alfabético.

---

## Funciones Generales

### `float(valor)`
**¿Qué realiza?**  
Convierte un valor (string, número entero, etc.) a número de punto flotante (decimal).

**¿Qué retorna?**  
Un número decimal (float).

**Ejemplos típicos:**
```python
float("3.14")        # Retorna 3.14
float(5)             # Retorna 5.0
precio = float(input("Precio: "))  # Convierte entrada a decimal
```

### `input(mensaje)`
**¿Qué realiza?**  
Solicita entrada del usuario desde la consola. Muestra un mensaje y espera que el usuario escriba algo.

**¿Qué retorna?**  
Una cadena de texto (string) con lo que el usuario ingresó.

**Ejemplos típicos:**
```python
nombre = input("¿Cuál es tu nombre? ")  # "Juan"
numero = input("Ingresa un número: ")    # "42"
respuesta = input("¿Continuar? (s/n): ")  # "s"
```

### `int(valor)`
**¿Qué realiza?**  
Convierte un valor (string, número decimal, etc.) a número entero.

**¿Qué retorna?**  
Un número entero (int).

**Ejemplos típicos:**
```python
int("42")            # Retorna 42
int(3.14)            # Retorna 3 (trunca decimales)
edad = int(input("Tu edad: "))  # Convierte entrada a entero
47 // 5              # División entera, también retorna int
```

### `len(colección)`
**¿Qué realiza?**  
Retorna la cantidad de elementos en una colección (lista, string, tuple, diccionario, set).

**¿Qué retorna?**  
Un número entero (int) con la cantidad de elementos.

**Ejemplos típicos:**
```python
len([1, 2, 3])              # Retorna 3
len("Python")               # Retorna 6
len({"a": 1, "b": 2})      # Retorna 2 (número de claves)
len({1, 2, 3})             # Retorna 3 (cantidad de elementos en el set)
```

### `max(colección)` o `max(a, b, c, ...)`
**¿Qué realiza?**  
Retorna el elemento de mayor valor en una colección o entre los argumentos dados.

**¿Qué retorna?**  
El elemento máximo (mismo tipo que los elementos).

**Ejemplos típicos:**
```python
max([3, 1, 4, 1, 5])       # Retorna 5
max("abc")                 # Retorna "c"
max(10, 20, 5)             # Retorna 20
max(["Ana", "Juan", "Zoe"])  # Retorna "Zoe" (orden alfabético)
```

### `min(colección)` o `min(a, b, c, ...)`
**¿Qué realiza?**  
Retorna el elemento de menor valor en una colección o entre los argumentos dados.

**¿Qué retorna?**  
El elemento mínimo (mismo tipo que los elementos).

**Ejemplos típicos:**
```python
min([3, 1, 4, 1, 5])       # Retorna 1
min("abc")                 # Retorna "a"
min(10, 20, 5)             # Retorna 5
```

### `print(*objetos, sep=' ', end='\n')`
**¿Qué realiza?**  
Imprime valores en la consola. Puede mostrar múltiples valores separados por un separador.

**¿Qué retorna?**  
None (no retorna valor, solo realiza la acción de imprimir).

**Ejemplos típicos:**
```python
print("Hola")              # Imprime: Hola
print(42)                  # Imprime: 42
print("Nombre:", "Juan")   # Imprime: Nombre: Juan
print(1, 2, 3, sep="-")    # Imprime: 1-2-3
print("Sin salto", end="") # No agrega salto de línea
```

### `range(inicio, fin, paso)`
**¿Qué realiza?**  
Genera una secuencia de números desde inicio hasta fin-1 con un paso determinado.

**¿Qué retorna?**  
Un objeto range (iterable) que puede convertirse a lista.

**Ejemplos típicos:**
```python
list(range(5))          # Retorna [0, 1, 2, 3, 4]
list(range(1, 6))       # Retorna [1, 2, 3, 4, 5]
list(range(0, 10, 2))   # Retorna [0, 2, 4, 6, 8]
for i in range(3):      # Itera 0, 1, 2
    print(i)
```

### `sorted(colección, reverse=False)`
**¿Qué realiza?**  
Retorna una nueva lista con los elementos ordenados. No modifica la colección original.

**¿Qué retorna?**  
Una lista con los elementos ordenados.

**Ejemplos típicos:**
```python
sorted([3, 1, 4, 1, 5])         # Retorna [1, 1, 3, 4, 5]
sorted("python")                # Retorna ['h', 'n', 'o', 'p', 't', 'y']
sorted(["Ana", "Juan"], reverse=True)  # Retorna ['Juan', 'Ana']
sorted({3, 1, 2})               # Retorna [1, 2, 3]
```

### `sum(colección, inicio=0)`
**¿Qué realiza?**  
Suma todos los elementos numéricos en una colección, comenzando desde un valor inicial.

**¿Qué retorna?**  
Un número (int o float) con la suma total.

**Ejemplos típicos:**
```python
sum([1, 2, 3, 4])               # Retorna 10
sum([1.5, 2.5, 3.0])            # Retorna 7.0
sum(range(1, 6))                # Retorna 15 (suma 1+2+3+4+5)
sum([1, 2, 3], 10)              # Retorna 16 (comienza en 10)
sum(x**2 for x in range(11) if x % 2 == 0)  # Suma cuadrados de pares
```

---

## Funciones para Strings (Cadenas de Texto)

### `string.isdigit()`
**¿Qué realiza?**  
Verifica si todos los caracteres del string son dígitos (0-9).

**¿Qué retorna?**  
True si todos son dígitos, False en caso contrario.

**Ejemplos típicos:**
```python
"123".isdigit()         # Retorna True
"12.3".isdigit()        # Retorna False (tiene punto)
"abc".isdigit()         # Retorna False
"".isdigit()            # Retorna False (string vacío)
if input("Número: ").isdigit():  # Valida entrada numérica
    numero = int(...)
```

### `string.lower()`
**¿Qué realiza?**  
Convierte todos los caracteres del string a minúsculas.

**¿Qué retorna?**  
Un nuevo string con todos los caracteres en minúsculas.

**Ejemplos típicos:**
```python
"PYTHON".lower()        # Retorna "python"
"HeLLo WoRLd".lower()   # Retorna "hello world"
entrada = input("¿Continuar? (s/n): ").lower()  # Normaliza entrada
if entrada == "s":
    # Continuar
```

### `string.split(separador)`
**¿Qué realiza?**  
Divide el string en partes usando un separador y retorna una lista.

**¿Qué retorna?**  
Una lista de strings (substrings divididos).

**Ejemplos típicos:**
```python
"uno,dos,tres".split(",")       # Retorna ['uno', 'dos', 'tres']
"Python es genial".split()      # Retorna ['Python', 'es', 'genial']
"a-b-c-d".split("-")            # Retorna ['a', 'b', 'c', 'd']
linea = input("Ingresa 3 números: ").split()
numeros = [int(x) for x in linea]
```

### `string.upper()`
**¿Qué realiza?**  
Convierte todos los caracteres del string a mayúsculas.

**¿Qué retorna?**  
Un nuevo string con todos los caracteres en mayúsculas.

**Ejemplos típicos:**
```python
"python".upper()        # Retorna "PYTHON"
"HeLLo WoRLd".upper()   # Retorna "HELLO WORLD"
mensaje = "Atención".upper()  # Retorna "ATENCIÓN"
```

---

## Funciones para Listas

### `lista.append(elemento)`
**¿Qué realiza?**  
Añade un elemento al final de la lista. Modifica la lista original.

**¿Qué retorna?**  
None (modifica la lista en su lugar, no retorna valor).

**Ejemplos típicos:**
```python
numeros = [1, 2, 3]
numeros.append(4)       # numeros ahora es [1, 2, 3, 4]

nombres = []
nombres.append("Ana")
nombres.append("Juan")  # nombres es ["Ana", "Juan"]

# Uso común en bucles
lista = []
for i in range(5):
    lista.append(i * 2)  # Construye [0, 2, 4, 6, 8]
```

---

## Funciones para Diccionarios

### `diccionario.get(clave, por_defecto=None)`
**¿Qué realiza?**  
Obtiene el valor asociado a una clave. Si la clave no existe, retorna un valor por defecto.

**¿Qué retorna?**  
El valor asociado a la clave, o el valor por defecto si no existe.

**Ejemplos típicos:**
```python
datos = {"nombre": "Juan", "edad": 25}
datos.get("nombre")         # Retorna "Juan"
datos.get("ciudad")         # Retorna None
datos.get("ciudad", "N/A")  # Retorna "N/A"

# Uso seguro para evitar KeyError
if diccionario.get("clave"):
    # Hacer algo
```

### `diccionario.items()`
**¿Qué realiza?**  
Retorna todos los pares clave-valor del diccionario como tuplas.

**¿Qué retorna?**  
Un objeto dict_items (iterable) con pares (clave, valor).

**Ejemplos típicos:**
```python
productos = {"pan": 2.50, "leche": 3.20, "queso": 5.00}
for nombre, precio in productos.items():
    print(f"{nombre}: ${precio:.2f}")
# Salida:
# pan: $2.50
# leche: $3.20
# queso: $5.00

list(productos.items())  # Retorna [('pan', 2.5), ('leche', 3.2), ...]
```

### `diccionario.values()`
**¿Qué realiza?**  
Retorna todos los valores del diccionario.

**¿Qué retorna?**  
Un objeto dict_values (iterable) con todos los valores.

**Ejemplos típicos:**
```python
calificaciones = {"María": 9.5, "Pedro": 8.0, "Ana": 9.0}
calificaciones.values()     # dict_values([9.5, 8.0, 9.0])
list(calificaciones.values())  # Retorna [9.5, 8.0, 9.0]
promedio = sum(calificaciones.values()) / len(calificaciones)
```

---

## Funciones para Sets (Conjuntos)

### `conjunto.add(elemento)`
**¿Qué realiza?**  
Añade un elemento al conjunto. Si el elemento ya existe, no hace nada (sets no admiten duplicados).

**¿Qué retorna?**  
None (modifica el conjunto en su lugar, no retorna valor).

**Ejemplos típicos:**
```python
unicos = {"Ana", "Juan", "Pedro"}
unicos.add("Lucía")     # unicos es {"Ana", "Juan", "Pedro", "Lucía"}
unicos.add("Ana")       # No hace nada, "Ana" ya existe

# Uso común para eliminar duplicados
nombres = ["Ana", "Juan", "Ana", "María", "Juan"]
unicos = set()
for nombre in nombres:
    unicos.add(nombre)  # unicos es {"Ana", "Juan", "María"}
```

---

## Resumen de Funciones por Categoría

| Categoría | Funciones |
|-----------|-----------|
| **Generales** | float, input, int, len, max, min, print, range, sorted, sum |
| **Strings** | isdigit, lower, split, upper |
| **Listas** | append |
| **Diccionarios** | get, items, values |
| **Sets** | add |

---

## Notas Importantes

- **Métodos vs Funciones**: Los métodos se llaman sobre objetos (ej: `lista.append()`), mientras que las funciones se llaman directamente (ej: `len(lista)`).
- **Modificación en lugar**: Algunos métodos como `append()` modifican el objeto original. Otros como `sorted()` retornan un nuevo objeto sin modificar el original.
- **PEP 8**: En este documento se respetan los estándares de formato de código Python (máximo 79 caracteres por línea).
- **Importancia de estas funciones**: Son fundamentales para trabajar con colecciones (listas, diccionarios, tuplas, sets) en Python.
