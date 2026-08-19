# Funciones Utilizadas en capitulo_04_Bucles

Documento que agrupa todas las funciones (built-in y métodos) utilizadas en los ejercicios y enunciados, organizadas por tipo de dato y en orden alfabético.

---

## Funciones Generales

### `enumerate(colección, inicio=0)`
**¿Qué realiza?**  
Itera sobre una colección proporcionando índice y elemento simultáneamente.

**¿Qué retorna?**  
Un objeto enumerate (iterable) con pares (índice, elemento).

**Ejemplos típicos:**
```python
numeros = ["a", "b", "c"]
for i, valor in enumerate(numeros):
    print(f"{i}: {valor}")  # 0: a, 1: b, 2: c

list(enumerate(['x', 'y', 'z']))
# Retorna [(0, 'x'), (1, 'y'), (2, 'z')]
```

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
float("-2.5")        # Retorna -2.5
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
Retorna la cantidad de elementos en una colección (lista, string, tuple, etc.).

**¿Qué retorna?**  
Un número entero (int) con la cantidad de elementos.

**Ejemplos típicos:**
```python
len([1, 2, 3])              # Retorna 3
len("Python")               # Retorna 6
len({"a": 1, "b": 2})      # Retorna 2 (número de claves)
len({1, 2, 3})             # Retorna 3
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
max(["Ana", "Juan", "Zoe"])  # Retorna "Zoe"
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
sorted("python")                # Retorna ['h', 'n', 'o', ...]
sorted(["Ana", "Juan"], reverse=True)
# Retorna ['Juan', 'Ana']
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
sum(range(1, 6))                # Retorna 15
sum([1, 2, 3], 10)              # Retorna 16
```

### `zip(colección1, colección2, ...)`
**¿Qué realiza?**  
Agrupa elementos correspondientes de múltiples secuencias en tuplas.

**¿Qué retorna?**  
Un objeto zip (iterable) con tuplas de elementos pareados.

**Ejemplos típicos:**
```python
numeros = [1, 2, 3]
letras = ['a', 'b', 'c']
list(zip(numeros, letras))
# Retorna [(1, 'a'), (2, 'b'), (3, 'c')]

for num, letra in zip([1, 2, 3], ['a', 'b', 'c']):
    print(f"{num}: {letra}")  # 1: a, 2: b, 3: c
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

lista = []
for i in range(5):
    lista.append(i * 2)  # Construye [0, 2, 4, 6, 8]
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
if input("Número: ").isdigit():
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
entrada = input("¿Continuar? (s/n): ").lower()
if entrada == "s":
    # Continuar
```

### `string.replace(viejo, nuevo)`
**¿Qué realiza?**  
Reemplaza todas las ocurrencias de un substring por otro.

**¿Qué retorna?**  
Un nuevo string con los reemplazos realizados.

**Ejemplos típicos:**
```python
"Python es genial".replace("genial", "excelente")
# Retorna "Python es excelente"

"aaa".replace("a", "b")  # Retorna "bbb"
texto = "hola hola".replace("hola", "adiós")
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
linea = input("Ingresa números: ").split()
numeros = [int(x) for x in linea]
```

### `string.startswith(prefijo)`
**¿Qué realiza?**  
Verifica si el string comienza con un substring específico.

**¿Qué retorna?**  
True si comienza con el substring, False en caso contrario.

**Ejemplos típicos:**
```python
"Python".startswith("Py")       # Retorna True
"Python".startswith("python")   # Retorna False
"archivo.txt".startswith("archivo")  # Retorna True
if nombre.startswith("A"):
    print("Comienza con A")
```

---

## Resumen de Funciones por Categoría

| Categoría | Funciones |
|-----------|-----------|
| **Generales** | enumerate, float, input, int, len, max, min, print, range, sorted, sum, zip |
| **Listas** | append |
| **Strings** | isdigit, lower, replace, split, startswith |

---

## Notas Importantes

- **Métodos vs Funciones**: Los métodos se llaman sobre objetos (ej: `lista.append()`), mientras que las funciones se llaman directamente (ej: `len(lista)`).
- **Modificación en lugar**: Algunos métodos como `append()` modifican el objeto original. Otros como `sorted()` retornan un nuevo objeto.
- **PEP 8**: En este documento se respetan los estándares de formato de código Python (máximo 79 caracteres por línea).
- **Importancia de estas funciones**: Son fundamentales para trabajar con bucles, iteración y manipulación de datos en Python.
