# Metodología de trabajo --- Programación 2

Este documento describe la metodología de trabajo utilizada en
**Programación 2** de la TECNICATURA Universitaria en Programación.

Tiene un doble propósito:

- informar a los estudiantes cómo se organizarán los proyectos y el
  trabajo colaborativo durante la cursada;
- dejar documentada la experiencia para los docentes de las materias
  posteriores, especialmente **Programación 3**, de manera que
  conozcan las prácticas y competencias con las que los estudiantes
  llegan a la asignatura.

------------------------------------------------------------------------

## 1. Enfoque general

Durante Programación 2 no se utilizará GitHub solamente como medio para
entregar trabajos terminados.

Git y GitHub formarán parte de la metodología de desarrollo y también
del proceso de aprendizaje.

Además del resultado final será importante el **proceso mediante el cual
ese resultado fue construido**.

Se trabajará con:

- repositorios Git;
- repositorios remotos privados en GitHub;
- ramas;
- commits frecuentes;
- desarrollo individual dentro de un proyecto grupal;
- comparación de soluciones;
- integración progresiva;
- Pull Requests;
- revisión de código;
- seguimiento del historial de desarrollo.

------------------------------------------------------------------------

## 2. Organización general en GitHub

La materia utiliza una organización de GitHub administrada por la
cátedra.

El repositorio general contiene el material común:

``` text
05-programacion-2/
│
├── README.md
├── METODOLOGIA_DE_TRABAJO.md
└── MATERIAL/
    └── MANUAL/
```

Los proyectos de los estudiantes **no se desarrollarán directamente en
este repositorio**.

------------------------------------------------------------------------

## 3. Organización de los grupos

Los estudiantes trabajarán en grupos de **3 o 4 integrantes, ni menos ni
más**.

Las comisiones son:

- **TUP11**
- **TUP13**

Cada grupo dispondrá de su propio repositorio privado dentro de la
organización de GitHub de la cátedra.

Por ejemplo:

``` text
p2-2026-banco-tup11-g01
p2-2026-banco-tup11-g02
p2-2026-banco-tup13-g01
```

Cada grupo podrá acceder solamente a su propio repositorio. Un grupo no
podrá consultar el código de otro grupo.

Los docentes podrán acceder a todos los repositorios para acompañar y
observar el proceso de aprendizaje.

------------------------------------------------------------------------

## 4. Proyecto Banco: mismo problema, soluciones independientes

El primer proyecto integrador será el **Proyecto Banco**.

Todos los grupos:

- recibirán el mismo enunciado;
- trabajarán sobre los mismos objetivos;
- tendrán las mismas cinco iteraciones;
- dispondrán del mismo tiempo;
- partirán desde cero;
- desarrollarán su propia solución.

No se proporcionará una solución inicial para completar.

Cada grupo construirá independientemente su programa y no tendrá acceso
a las soluciones de los demás grupos durante el desarrollo.

El proyecto se realizará en **Python**, sin base de datos, sin Django,
sin frontend y sin interfaz web.

El propósito de esta etapa es concentrarse en Programación Orientada a
Objetos, lógica de negocio, organización del código y trabajo con Git.

------------------------------------------------------------------------

## 5. Cinco iteraciones de una semana

El Proyecto Banco se desarrollará mediante **5 iteraciones**, con una
duración prevista de **una semana por iteración**.

Cada iteración parte del estado integrado alcanzado en la anterior y
agrega los conceptos de POO trabajados durante esa etapa de la materia.

El proyecto, por lo tanto, no se construye de una sola vez:

``` text
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
Proyecto integrado
```

Las limitaciones de una iteración pueden ser deliberadas. Una versión
puede permitir situaciones que todavía no sabemos resolver correctamente
porque el concepto necesario será incorporado en la iteración siguiente.

Esto permite observar **por qué aparece la necesidad de un nuevo
concepto de POO**, y no solamente aprender su sintaxis.

------------------------------------------------------------------------

## 6. Principio fundamental: todos realizan toda la iteración

Durante estas cinco iteraciones **no se dividirá el aprendizaje de POO
en partes diferentes para cada integrante**.

No se busca una distribución como:

``` text
Integrante A → constructor
Integrante B → depositar
Integrante C → extraer
Integrante D → __str__
```

Ese reparto puede producir un programa terminado, pero no garantiza que
todos hayan recorrido el mismo problema.

La metodología será:

``` text
Integrante A → iteración completa
Integrante B → iteración completa
Integrante C → iteración completa
Integrante D → iteración completa
```

En un grupo de tres integrantes, los tres realizan la iteración
completa.

De esta forma todos enfrentan una carga conceptual comparable y todos
deben aplicar los contenidos trabajados durante la semana.

------------------------------------------------------------------------

## 7. Ramas individuales por iteración

La rama `main` representará siempre la **última versión integrada y
aceptada por el grupo**.

Al comenzar una nueva iteración, cada integrante partirá de `main`
actualizada y creará su propia rama.

El formato será:

``` text
iteracion-NN/nombre-apellido
```

Por ejemplo:

``` text
main
│
├── iteracion-01/juan-perez
├── iteracion-01/ana-gomez
├── iteracion-01/pedro-lopez
└── iteracion-01/maria-diaz
```

Cada una de esas ramas contiene una **solución completa de la misma
iteración**.

No son ramas donde cada alumno resuelve una funcionalidad diferente.

------------------------------------------------------------------------

## 8. Etapa individual

Al comenzar la iteración:

``` bash
git switch main
git pull
git switch -c iteracion-01/nombre-apellido
```

Cada estudiante deberá:

1. interpretar el enunciado;
2. desarrollar la solución completa;
3. probar su código;
4. realizar commits durante el proceso;
5. publicar periódicamente su rama en GitHub.

La primera publicación de la rama será, por ejemplo:

``` bash
git push -u origin iteracion-01/nombre-apellido
```

Después:

``` bash
git push
```

será suficiente para publicar nuevos commits.

### Regla de trabajo individual

Durante esta etapa cada estudiante deberá intentar resolver la iteración
**antes de consultar las ramas de sus compañeros**.

La comparación de soluciones pertenece a la etapa posterior.

El objetivo no es competir entre integrantes sino garantizar que todos
hayan tenido que pensar y resolver personalmente el problema.

------------------------------------------------------------------------

## 9. Commits durante la solución individual

No se espera un único commit con todo el trabajo de la semana.

Se realizarán commits que representen avances identificables.

Por ejemplo, en una primera iteración podrían aparecer:

``` text
Agrega estructura inicial de Cuenta
Implementa constructor de Cuenta
Implementa depósito y extracción
Agrega representación con __str__
Agrega casos de prueba
```

Se evitarán mensajes como:

``` text
cambios
cosas
prueba
final
```

La cantidad de commits por sí sola **no constituye una medida de
aprendizaje ni una calificación**.

El historial permite observar cómo evolucionó la solución.

------------------------------------------------------------------------

## 10. Fin de la etapa individual

Antes de comenzar la integración, todos los integrantes deberán tener
publicada su solución individual.

En ese momento el repositorio podría mostrar:

``` text
main
│
├── iteracion-01/juan-perez
├── iteracion-01/ana-gomez
├── iteracion-01/pedro-lopez
└── iteracion-01/maria-diaz
```

A partir de este punto comienza formalmente la comparación grupal.

Las soluciones individuales se conservarán como evidencia del proceso de
aprendizaje.

------------------------------------------------------------------------

## 11. Comparación y revisión entre compañeros

Una vez finalizada la etapa individual, los integrantes podrán consultar
y comparar las distintas soluciones.

La pregunta no será:

> ¿Quién hizo el código que vamos a usar?

La pregunta será:

> ¿Qué decisiones de cada solución nos ayudan a construir la mejor
> versión integrada que el grupo puede justificar?

El grupo deberá observar, entre otras cosas:

- claridad del código;
- nombres elegidos;
- responsabilidades de las clases;
- métodos implementados;
- uso correcto de los conceptos de la iteración;
- pruebas realizadas;
- diferencias de diseño;
- código innecesario;
- soluciones que se adelantaron a contenidos todavía no trabajados.

Comparar soluciones forma parte de la actividad.

------------------------------------------------------------------------

## 12. Pull Requests individuales para revisión

Cada integrante podrá abrir un Pull Request desde su rama individual
hacia `main` para facilitar la revisión de:

- commits;
- archivos modificados;
- diferencias de código;
- comentarios de los compañeros.

Por ejemplo:

``` text
iteracion-01/juan-perez → main
iteracion-01/ana-gomez  → main
iteracion-01/pedro-lopez → main
```

Estos Pull Requests individuales tienen como finalidad **comparar y
revisar**.

**No deben fusionarse directamente con `main`**, salvo indicación
expresa de la cátedra.

Una vez realizada la comparación podrán cerrarse sin merge.

------------------------------------------------------------------------

## 13. Rama de integración

Después de comparar las soluciones, el grupo creará:

``` text
integracion/iteracion-01
```

Esta rama contendrá la solución consensuada.

No se trata simplemente de elegir la solución de uno de los integrantes.

El grupo deberá decidir qué diseño conservar, qué modificar y cómo
construir una versión que todos puedan explicar.

El esquema es:

``` text
                 iteracion-01/alumno-a
                /
main ──────────┼── iteracion-01/alumno-b
                \
                 iteracion-01/alumno-c
                         │
                         ↓
                    comparación
                         │
                         ↓
              integracion/iteracion-01
                         │
                         ↓
                    Pull Request
                         │
                         ↓
                        main
```

------------------------------------------------------------------------

## 14. Responsable de integración

Para distribuir también la experiencia de integración, el grupo tendrá
un **responsable de integración** en cada iteración.

Su función no es decidir solo ni reemplazar el trabajo del resto.

Será responsable de:

- crear o coordinar la rama de integración;
- aplicar las decisiones consensuadas;
- verificar que la versión integrada funcione;
- abrir el Pull Request de integración;
- coordinar las correcciones que surjan de la revisión.

La responsabilidad deberá rotar entre los integrantes a lo largo de las
iteraciones.

En grupos de cuatro puede utilizarse, por ejemplo:

``` text
Iteración 1 → integrante A
Iteración 2 → integrante B
Iteración 3 → integrante C
Iteración 4 → integrante D
Iteración 5 → integración conjunta
```

En grupos de tres la responsabilidad también deberá rotarse.

------------------------------------------------------------------------

## 15. Pull Request de integración

Cuando la solución grupal esté terminada:

``` text
integracion/iteracion-01 → main
```

se abrirá el Pull Request que propone la versión oficial de la
iteración.

Antes del merge el grupo deberá poder explicar:

- qué diferencias encontraron entre las soluciones;
- qué decisiones adoptaron;
- por qué las adoptaron;
- qué problemas encontraron;
- qué aprendieron durante la integración.

Una vez revisada y aceptada, la rama se fusionará con `main`.

`main` pasa entonces a representar el **estado oficial del Proyecto
Banco al final de esa iteración**.

------------------------------------------------------------------------

## 16. Comienzo de la iteración siguiente

La siguiente iteración comienza desde la versión integrada.

Todos los estudiantes deberán actualizar `main`:

``` bash
git switch main
git pull
```

Y crear nuevamente su rama individual:

``` bash
git switch -c iteracion-02/nombre-apellido
```

El ciclo se repite:

``` text
main actualizada
      ↓
soluciones individuales completas
      ↓
commits y push
      ↓
comparación
      ↓
integracion/iteracion-02
      ↓
Pull Request
      ↓
main
```

Esto continuará hasta completar las cinco iteraciones.

------------------------------------------------------------------------

## 17. Seguimiento docente

El docente podrá consultar los repositorios durante todo el proceso.

El seguimiento podrá considerar:

- existencia de una solución individual por integrante;
- evolución de cada solución;
- commits y autores;
- frecuencia de actualización;
- comprensión de los conceptos trabajados;
- participación en revisiones;
- comparación de alternativas;
- Pull Requests;
- integración;
- rotación del responsable de integración;
- capacidad de explicar las decisiones tomadas.

El objetivo no es convertir la actividad de GitHub en una calificación
automática.

Git aporta evidencia para comprender mejor **cómo está aprendiendo y
trabajando cada estudiante**.

------------------------------------------------------------------------

## 18. Equilibrio de participación

El proyecto es grupal, pero durante las cinco iteraciones iniciales
todos los integrantes deben atravesar una experiencia comparable.

Por eso:

- todos resuelven la misma iteración;
- todos programan;
- todos realizan commits;
- todos publican su rama;
- todos leen código de compañeros;
- todos participan de la discusión de integración;
- todos deben poder explicar la versión final;
- la responsabilidad de integración rota.

No se considerará suficiente que un integrante conozca solamente la
parte del programa que escribió.

------------------------------------------------------------------------

## 19. Articulación con Programación 3

Esta metodología deja documentado no solamente qué contenidos fueron
trabajados, sino **cómo fueron trabajados**.

Al finalizar estas iteraciones, los estudiantes habrán tenido
experiencia en:

- resolución individual de problemas de POO;
- evolución incremental de un mismo sistema;
- lectura de código ajeno;
- comparación de diseños;
- argumentación sobre decisiones de programación;
- control de versiones;
- ramas;
- commits;
- repositorios remotos;
- Pull Requests;
- integración de soluciones;
- resolución de conflictos propios del trabajo colaborativo.

Esto permite que los docentes de **Programación 3** conozcan el punto de
partida metodológico de los estudiantes y puedan decidir qué prácticas
continuar, profundizar o reforzar.

No implica asumir que todos alcanzarán el mismo nivel de autonomía.

------------------------------------------------------------------------

## 20. Proyectos posteriores

Más adelante podrán realizarse otros proyectos y utilizar una
organización más cercana al desarrollo profesional por funcionalidades,
por ejemplo:

``` text
feature/alta-cliente
feature/crear-cuenta
feature/transferencia
```

En ese momento sí podrá distribuirse el trabajo entre funcionalidades
diferentes.

La diferencia es intencional:

``` text
Primeras iteraciones de POO
        ↓
todos resuelven el problema completo
        ↓
objetivo: aprendizaje individual + integración

Proyectos posteriores
        ↓
división por funcionalidades
        ↓
objetivo: desarrollo colaborativo especializado
```

De esta manera, la metodología de Git acompaña el objetivo pedagógico de
cada etapa en lugar de imponer una única forma de trabajo.

------------------------------------------------------------------------

## 21. Principio general

El objetivo no es solamente que el Proyecto Banco funcione.

Se busca que cada estudiante pueda decir:

> **Lo programé, lo comparé con otras soluciones, discutí las decisiones
> y participé en la construcción de la versión integrada.**

Durante Programación 2 se busca avanzar desde:

``` text
"escribir un programa"
```

hacia:

``` text
"comprender, construir, revisar e integrar software con otros"
```

El código final es una parte del aprendizaje.

También forman parte del aprendizaje el razonamiento individual, la
comparación de alternativas, la revisión, la integración, la
comunicación y la capacidad de explicar las decisiones tomadas.
