# Funciones Utilizadas en capitulo_03_Condicional

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

---

## Funciones para Strings (Cadenas de Texto)

### `string.isalpha()`
**¿Qué realiza?**  
Verifica si todos los caracteres del string son letras alfabéticas.

**¿Qué retorna?**  
True si todos son letras, False en caso contrario.

**Ejemplos típicos:**
```python
"abc".isalpha()         # Retorna True
"123".isalpha()         # Retorna False
"abc123".isalpha()      # Retorna False
"".isalpha()            # Retorna False (string vacío)
```

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

### `string.strip()`
**¿Qué realiza?**  
Elimina espacios en blanco al inicio y final del string.

**¿Qué retorna?**  
Un nuevo string sin espacios en los extremos.

**Ejemplos típicos:**
```python
"  Python  ".strip()      # Retorna "Python"
"\thello\n".strip()       # Retorna "hello"
entrada = input("Nombre: ").strip()
"  123  ".strip()         # Retorna "123"
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

## Resumen de Funciones por Categoría

| Categoría | Funciones |
|-----------|-----------|
| **Generales** | float, input, int, max, print |
| **Strings** | isalpha, isdigit, lower, replace, strip, upper |

---

## Notas Importantes

- **Métodos vs Funciones**: Los métodos se llaman sobre objetos (ej: `string.lower()`), mientras que las funciones se llaman directamente (ej: `len(string)`).
- **Modificación en lugar**: Algunos métodos modifican el objeto original. Otros retornan un nuevo objeto sin modificar el original.
- **PEP 8**: En este documento se respetan los estándares de formato de código Python (máximo 79 caracteres por línea).
- **Importancia de estas funciones**: Son fundamentales para trabajar con operaciones básicas y manipulación de strings en Python.
