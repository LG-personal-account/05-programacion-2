# Semana 1 — Tips y demos en el shell de Python

---

## CAP. 1 — Ecosistema Python (0:00 - 0:30)

**Estilo PEP 8**

1. Indentación: 4 espacios (nunca tab)
2. `snake_case` para variables y funciones
3. `UPPER_CASE` para constantes
4. `PascalCase` para clases
5. Máximo 79 caracteres por línea
6. Espacios alrededor de operadores (`x = 5 + 3`, no `x=5+3`)
7. Docstrings con triple comilla `"""` para documentar funciones
8. Imports agrupados: biblioteca estándar → terceros → propios

**Verificación de entorno en clase**

```bash
python --version
python -m venv .venv
.venv\Scripts\activate       # Windows
source .venv/bin/activate    # Linux/Mac
```

---

## CAP. 2 — Datos, tipos y expresiones (0:30 - 1:30)

**REPL — Read Eval Print Loop**

```python
# Abrir el shell
python
>>>
```

**Variables — etiquetas, no cajas**

En C, una variable *es* una caja de memoria de tipo fijo.  
En Python, una variable es una *etiqueta* que apunta a un objeto.

```python
>>> x = 10
>>> x = "hola"      # válido: la etiqueta ahora apunta a otro objeto
>>> x = 3.14        # válido de nuevo
```

---

**Tipos**

**A — ENTEROS: precisión arbitraria**

```python
>>> 10 ** 100       # googol, no hay overflow
>>> type(10 ** 100)
```

**B — FLOAT: 64 bits, IEEE 754**

```python
>>> 10 / 2          # siempre devuelve float: 5.0
>>> 10 // 3         # división entera: 3
>>> 10 % 3          # módulo (resto): 1
>>> 2 ** 8          # potencia: 256
```

> **Diferencia clave con C:** `/` en Python *siempre* devuelve float.
> En C, `10 / 3` devuelve `3`. En Python devuelve `3.3333...`

**C — BOOLEAN: True y False con mayúscula**

Internamente son `1` y `0`.

```python
>>> a = 1
>>> b = True
>>> print(a, b)
1 True
>>> c = a + b
>>> print(c)
2
```

**D — STR: cadenas de texto**

```python
>>> nombre = "Ana"
>>> nombre = 'Ana'      # comillas simples o dobles, indistinto
>>> len(nombre)
3
```

---

**Función `type()`**

```python
>>> type(a)
<class 'int'>
>>> type(b)
<class 'bool'>
>>> type(c)
<class 'int'>
>>> type(3.14)
<class 'float'>
>>> type("hola")
<class 'str'>
```

---

**Entrada y salida — f-strings**

```python
>>> print("Hola mundo")
>>> print(f"a={a}, b={b}, c={c}")

# Comillas dobles afuera → comillas simples adentro
>>> print(f'La variable "a" guardó {a}.')

# Comillas simples afuera → comillas dobles adentro
>>> print(f"La variable 'a' guardó {a}.")

# Formato numérico
>>> precio = 1234.5678
>>> print(f"Precio: ${precio:.2f}")
```

---

**PROHIBIDO: `eval()`**

```python
>>> expresion = input("Ingrese un valor: ")
Ingrese un valor: __import__("os").getcwd()
>>> resultado = eval(expresion)
>>> resultado
# Ejecutó código arbitrario en tu sistema. Nunca en producción.
```

> `eval()` ejecuta cualquier cosa que el usuario escriba como código Python.  
> Siempre convertir con `int()`, `float()` o `str()`.

---

**IPython — laboratorio interactivo**

```bash
pip install ipython
ipython
# o en Windows:
py -m IPython
```

```python
In [1]: texto = "hola"

In [2]: texto.      # presionar TAB: lista todos los métodos disponibles
capitalize()   endswith()     index()        isdigit()      isspace()      lower()
casefold()     expandtabs()   isalnum()      isidentifier() istitle()      lstrip()
center()       find()         isalpha()      islower()      isupper()      maketrans()
count()        format()       isascii()      isnumeric()    join()         partition()
encode()       format_map()   isdecimal()    isprintable()  ljust()        removeprefix()
```

---

## CAP. 3 — Control de flujo condicional (1:30 - 2:45)

**Diferencias clave con C**

| C | Python |
|---|---|
| `if (edad >= 18) {` | `if edad >= 18:` |
| Llaves `{}` para bloques | Indentación obligatoria |
| `&&`, `\|\|`, `!` | `and`, `or`, `not` |
| `else if` | `elif` |
| `switch/case` | `match/case` (desde Python 3.10) |

---

**if / elif / else**

```python
>>> edad = 20
>>> if edad >= 18:
...     print("Mayor de edad")
... elif edad >= 13:
...     print("Adolescente")
... else:
...     print("Niño")
...
Mayor de edad
```

> Los `...` los muestra Python solo: indican que la instrucción no terminó.
> Vos solo escribís el código, sin los `>>>` ni los `...`.

---

**Operadores lógicos — con palabras, sin paréntesis**

```python
>>> a = 5
>>> b = 10
>>> a > 0 and b > 0
True
>>> a > 100 or b > 0
True
>>> not (a > 100)
True
```

**Comparaciones encadenadas — exclusivo de Python**

```python
>>> x = 15
>>> 10 <= x <= 20       # equivale a: x >= 10 and x <= 20
True
# En C necesitarías: (x >= 10 && x <= 20)
```

---

**match / case — el nuevo switch (Python 3.10+)**

```python
>>> dia = "miércoles"
>>> match dia.capitalize():
...     case "Lunes":
...         print("Inicio de semana")
...     case "Miércoles":
...         print("Mitad de semana")
...     case "Martes" | "Jueves" | "Viernes" | "Sábado" | "Domingo":
...         print("Día normal")
...     case _:
...         print("Dato no válido")
...
Mitad de semana
```

> El `|` dentro de un `case` funciona como `or`:
> *"si el valor es Martes, o Jueves, o Viernes..."*

> Diferencias con el `switch` de C:
> - No hay `break` (no existe fall-through en Python)
> - El default es `case _` (guión bajo)
> - Se escribe `match`, no `switch`

---

**Demo en vivo — clasificar día de la semana**

Escribir el archivo `dias.py` en VSCode, ejecutar desde terminal:

```python
dia = input("Ingresá un día: ").capitalize()

match dia:
    case "Lunes":
        print("Inicio de semana")
    case "Miércoles":
        print("Mitad de semana")
    case "Martes" | "Jueves" | "Viernes" | "Sábado" | "Domingo":
        print("Día normal")
    case _:
        print("Dato no válido")
```

> Error corregido respecto al manual original:
> "Lunes" **no** va en el tercer `case` porque ya fue capturado antes.
> Un `case` que nunca se alcanza es **código muerto**.

---

**isdigit() y negativos — trampa clásica**

```python
>>> "-5".isdigit()
False       # los negativos no pasan la validación

>>> "-5".lstrip("-").isdigit()
True        # alternativa: sacar el signo antes de preguntar

>>> # Mejor aún: usar try/except (lo vemos en el cap. 8)
```

> Esto conecta con el error del ejercicio de "Positivo/Cero/Negativo"
> del manual: con `isdigit()`, ningún número negativo llega a la rama
> `print("Negativo")`. La solución limpia viene en el capítulo 8.

---

## CAP. 4 — Bucles, listas y tuplas (2:45 - 4:00)

**Listas — colección ordenada y mutable**

```python
>>> notas = [7, 8, 5, 9, 6]

>>> notas[0]            # primer elemento
7
>>> notas[-1]           # último (índice negativo: no existe en C)
6
>>> notas[1:4]          # slicing: del índice 1 al 3 (el 4 no se incluye)
[8, 5, 9]
>>> notas[:3]           # los primeros 3
[7, 8, 5]
>>> notas[2:]           # desde el índice 2 hasta el final
[5, 9, 6]
>>> notas[::-1]         # lista al revés
[6, 9, 5, 8, 7]

>>> notas.append(10)    # agrega al final
>>> notas.remove(5)     # elimina el primer 5 que encuentre
>>> notas.pop()         # elimina y devuelve el último
>>> len(notas)          # cantidad de elementos
```

---

**Tuplas — colección ordenada e inmutable**

```python
>>> punto = (3, 5)
>>> punto[0]
3
>>> punto[0] = 10       # TypeError: las tuplas no se modifican
```

> Regla práctica: si los datos van a cambiar → lista.  
> Si son fijos (coordenadas, constantes, días de la semana) → tupla.

---

**while — casi idéntico a C**

```python
>>> i = 0
>>> while i < 5:
...     print(i)
...     i += 1          # Python no tiene i++
...
0
1
2
3
4
```

> Python **no tiene** `i++` ni `i--`.  
> Usar `i += 1` en su lugar.

**Patrón while True con break — equivalente al do-while de C**

```python
>>> while True:
...     dato = input("Ingresá un número (o 'fin'): ")
...     if dato == "fin":
...         break
...     print(f"Procesando: {dato}")
```

---

**for — el gran cambio respecto de C**

```python
# En C: for (int i = 0; i < 5; i++) { printf("%d\n", i); }

# En Python: el for recorre una colección
>>> notas = [7, 8, 5, 9, 6]
>>> for nota in notas:
...     print(nota)
...
7
8
5
9
6
```

> Leer en voz alta: *"para cada nota en notas, imprimí nota"*.  
> No hay índice, no hay condición de corte, no hay incremento manual.  
> Es imposible pasarse del final por error.

---

**range() — cuando sí necesitás contar**

```python
>>> list(range(5))              # [0, 1, 2, 3, 4]
>>> list(range(2, 8))           # [2, 3, 4, 5, 6, 7]
>>> list(range(0, 20, 2))       # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
>>> list(range(10, 0, -1))      # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

>>> for i in range(5):
...     print(i)
```

> El segundo argumento de `range()` **nunca se incluye**,
> igual que el slicing. Es una convención consistente en todo Python.

---

**enumerate() — índice y valor juntos**

```python
>>> nombres = ["Ana", "Juan", "Pedro"]
>>> for i, nombre in enumerate(nombres):
...     print(i, nombre)
...
0 Ana
1 Juan
2 Pedro

>>> for i, nombre in enumerate(nombres, start=1):   # empieza en 1
...     print(f"{i}. {nombre}")
...
1. Ana
2. Juan
3. Pedro
```

---

**zip() — dos listas en paralelo**

```python
>>> nombres = ["Ana", "Juan", "Pedro"]
>>> notas   = [8, 6, 9]
>>> for nombre, nota in zip(nombres, notas):
...     print(f"{nombre}: {nota}")
...
Ana: 8
Juan: 6
Pedro: 9
```

> Si las listas tienen distinto tamaño, `zip()` se detiene
> con la más corta. Sin error, sin índice fuera de rango.

---

**break y continue**

```python
# break — corta el bucle completo
>>> for n in [3, 7, 12, 5, 8]:
...     if n > 10:
...         print(f"Encontré uno mayor a 10: {n}")
...         break
...
Encontré uno mayor a 10: 12

# continue — saltea esta vuelta, sigue con la próxima
>>> for n in range(10):
...     if n % 2 != 0:
...         continue
...     print(n)
...
0
2
4
6
8
```

---

**for...else — rareza pythónica, útil para búsquedas**

```python
>>> buscado = 42
>>> for n in [3, 7, 12, 5, 8]:
...     if n == buscado:
...         print("Encontrado")
...         break
... else:
...     print(f"{buscado} no está en la lista")
...
42 no está en la lista
```

> El `else` es del `for`, no del `if`.  
> Se ejecuta **solo si el bucle terminó sin hacer `break`**.  
> Es la forma más limpia de escribir "buscar y avisar si no encontré nada".

---

**Demo en vivo — número primo con for...else**

```python
numero = int(input("Número: "))

if numero < 2:
    print("No es primo")
else:
    for divisor in range(2, numero):
        if numero % divisor == 0:
            print("No es primo")
            break
    else:
        print("Es primo")
```

> Probar con: 1, 2, 7, 9, 13, 100.  
> ¿Qué pasa con el 1? ¿Y con el 2?

---

**Funciones útiles para listas — sin for manual**

```python
>>> notas = [7, 4, 9, 6, 8, 3, 10, 5]
>>> len(notas)                      # 8
>>> sum(notas)                      # 52
>>> max(notas)                      # 10
>>> min(notas)                      # 3
>>> sorted(notas)                   # [3, 4, 5, 6, 7, 8, 9, 10] — lista nueva
>>> sorted(notas, reverse=True)     # [10, 9, 8, 7, 6, 5, 4, 3]
>>> notas.sort()                    # modifica la lista original, devuelve None
```

> Trampa clásica:
> ```python
> notas = notas.sort()    # notas queda en None
> ```
> `sort()` modifica en el lugar y **no devuelve nada**.  
> Si querés conservar la original: `ordenadas = sorted(notas)`.

---
