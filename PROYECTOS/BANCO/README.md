# Proyecto Integrador — Banco

## Programación 2

El **Proyecto Banco** es el primer proyecto integrador de Programación 2.

A lo largo de **5 iteraciones semanales** construiremos progresivamente un
sistema bancario utilizando los conceptos de Programación Orientada a Objetos
trabajados durante la materia.

El proyecto comienza deliberadamente con una solución muy sencilla. En cada
iteración aparecerán nuevos problemas y utilizaremos los conceptos aprendidos
para hacer evolucionar el sistema.

---

## Objetivo

El objetivo no es solamente llegar a un programa terminado.

Durante el proyecto cada estudiante deberá:

- desarrollar personalmente cada iteración completa;
- utilizar Git para registrar la evolución de su trabajo;
- trabajar con ramas;
- realizar commits frecuentes y descriptivos;
- publicar su trabajo en GitHub;
- comparar su solución con las de sus compañeros;
- participar en revisiones mediante Pull Requests;
- discutir decisiones de diseño;
- participar en la construcción de la solución integrada del grupo.

---

## Organización de los grupos

Los grupos estarán formados por **3 o 4 integrantes**.

Todos los grupos desarrollarán **el mismo Proyecto Banco**, pero cada grupo
trabajará en un repositorio privado independiente.

De esta manera:

- todos parten del mismo problema;
- todos tienen los mismos objetivos;
- todos disponen del mismo tiempo;
- cada grupo construye su propia solución;
- un grupo no puede consultar el código de los demás grupos.

---

## Regla fundamental

Durante las cinco iteraciones iniciales **no se divide el programa entre los
integrantes**.

No trabajaremos de esta manera:

```text
Integrante A → una clase
Integrante B → otra clase
Integrante C → validaciones
Integrante D → pruebas
```

Cada integrante deberá realizar **la iteración completa** en su propia rama:

```text
Integrante A → iteración completa
Integrante B → iteración completa
Integrante C → iteración completa
Integrante D → iteración completa
```

El objetivo es que todos atraviesen personalmente los mismos problemas y
apliquen los mismos conceptos de Programación Orientada a Objetos.

---

## Forma de trabajo de cada iteración

Cada semana se utilizará el siguiente ciclo:

```text
                 main
                  │
        ┌─────────┼─────────┐
        ↓         ↓         ↓
    alumno A   alumno B   alumno C
        │         │         │
        └─────────┼─────────┘
                  ↓
        comparación y revisión
                  ↓
       integración de la semana
                  ↓
           Pull Request
                  ↓
             revisión
                  ↓
                 main
```

En grupos de cuatro habrá cuatro ramas individuales.

---

## Ramas individuales

Cada estudiante creará una rama para la iteración.

Por ejemplo:

```text
iteracion-01/juan-perez
iteracion-01/ana-gomez
iteracion-01/pedro-lopez
```

Cada una deberá contener la solución completa desarrollada por ese
estudiante.

---

## Integración

Después de finalizar el trabajo individual, el grupo comparará las distintas
soluciones.

La versión grupal se construirá en una rama como:

```text
integracion/iteracion-01
```

La integración **no consiste simplemente en elegir el código de uno de los
integrantes**.

El grupo deberá analizar las soluciones, discutir las diferencias y construir
una versión que todos puedan comprender y explicar.

---

## Líder de integración

En cada iteración habrá un **líder de integración**.

El rol será rotativo.

El líder será responsable de:

- coordinar la revisión de las soluciones individuales;
- revisar los Pull Requests;
- solicitar correcciones cuando corresponda;
- coordinar la construcción de la solución integrada;
- verificar el funcionamiento de la versión grupal;
- abrir el Pull Request final de la iteración.

Ser líder no significa realizar el trabajo de los demás ni decidir
unilateralmente qué solución utilizar.

---

## Iteraciones

El proyecto se desarrollará durante cinco semanas.

### Iteración 1 — Clases y objetos

[Ver consigna de la Iteración 1](ITERACION_01.md)

Conceptos principales:

- clases;
- objetos;
- atributos;
- métodos;
- `self`;
- `__init__`;
- `__str__`;
- parámetros y valores por defecto.

### Iteración 2

La consigna será publicada al comenzar la segunda iteración.

### Iteración 3

La consigna será publicada al comenzar la tercera iteración.

### Iteración 4

La consigna será publicada al comenzar la cuarta iteración.

### Iteración 5

La consigna será publicada al comenzar la quinta iteración.

---

## Evolución del proyecto

Cada iteración parte de la versión integrada de la semana anterior:

```text
Iteración 1
     ↓
    main
     ↓
Iteración 2
     ↓
    main
     ↓
Iteración 3
     ↓
    main
     ↓
Iteración 4
     ↓
    main
     ↓
Iteración 5
     ↓
Proyecto Banco
```

Por esta razón es importante respetar los límites de cada consigna.

No se busca resolver anticipadamente problemas correspondientes a contenidos
que todavía no fueron trabajados.

---

## Repositorios

Este repositorio público contiene las **consignas y documentación común** del
Proyecto Banco.

El código de los estudiantes se desarrolla en repositorios privados
independientes para cada grupo.

El repositorio privado será utilizado para registrar todo el proceso de
trabajo:

```text
código
↓
commits
↓
ramas
↓
Pull Requests
↓
revisión
↓
integración
```

---

## Resultado esperado

Al finalizar las cinco iteraciones no buscamos solamente tener un sistema
bancario funcionando.

Cada estudiante deberá poder decir:

> Implementé cada etapa del proyecto, comparé mi solución con otras,
> participé en revisiones, discutí decisiones de diseño y colaboré en la
> construcción de la versión integrada de mi grupo.
