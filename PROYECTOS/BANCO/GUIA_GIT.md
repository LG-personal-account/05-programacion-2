# Guía Git --- Proyecto Integrador Banco

Esta guía explica el flujo de trabajo con Git y GitHub que utilizaremos
durante las cinco iteraciones del **Proyecto Integrador Banco**.

Está pensada para estudiantes que recién comienzan a trabajar con Git.

> **Importante:** durante estas primeras cinco iteraciones no
> dividiremos el proyecto por funcionalidades. Cada integrante
> desarrollará la iteración completa en su propia rama.

------------------------------------------------------------------------

## 1. Cómo está organizado el trabajo

Cada grupo trabaja en un repositorio privado propio.

Por ejemplo:

``` text
p2-banco-tup13-g01
```

Los integrantes del grupo tienen permiso para trabajar en ese
repositorio, pero no pueden consultar los repositorios privados de los
otros grupos.

La cátedra publica las consignas generales en el repositorio público de
Programación 2.

------------------------------------------------------------------------

## 2. El flujo de cada iteración

Supongamos un grupo de cuatro estudiantes.

Durante la Iteración 1 tendremos conceptualmente:

``` text
main
│
├── iteracion-01/alumno-a
├── iteracion-01/alumno-b
├── iteracion-01/alumno-c
├── iteracion-01/alumno-d
│
└── integracion/iteracion-01
```

Cada estudiante desarrolla **toda la iteración**.

Cuando termina su solución, abre un Pull Request hacia:

``` text
integracion/iteracion-01
```

El grupo compara las soluciones y construye una versión integrada.

Finalmente, el líder de la semana abre otro Pull Request:

``` text
integracion/iteracion-01
        ↓
       main
```

Ese Pull Request será revisado por la cátedra.

El flujo completo es:

``` text
ramas individuales
        │
        ├── Pull Requests
        ↓
integracion/iteracion-01
        │
        ├── Pull Request
        ↓
       main
```

------------------------------------------------------------------------

## 3. ¿Qué es una rama?

Una rama o **branch** permite trabajar sobre una versión del proyecto
sin modificar directamente la rama principal.

La rama principal del repositorio se llama:

``` text
main
```

Durante estas cinco iteraciones, cada estudiante tendrá una rama
personal por iteración.

Ejemplos:

``` text
iteracion-01/juan-perez
iteracion-01/ana-gomez
iteracion-01/pedro-lopez
```

En la siguiente semana se crearán nuevas ramas:

``` text
iteracion-02/juan-perez
iteracion-02/ana-gomez
iteracion-02/pedro-lopez
```

Las ramas de una nueva iteración siempre deben nacer de la versión de
`main` correspondiente a la iteración anterior.

------------------------------------------------------------------------

## 4. Preparar una carpeta local

Elegí una carpeta de tu computadora donde guardarás los proyectos de la
materia.

Por ejemplo:

``` text
Documentos/
└── Programacion-2/
```

No es necesario crear manualmente una carpeta para el repositorio: el
comando `git clone` puede crearla.

------------------------------------------------------------------------

## 5. Abrir la terminal en VS Code

Podés trabajar desde la terminal integrada de Visual Studio Code.

Menú:

``` text
Terminal → New Terminal
```

También podés utilizar Git Bash.

Los comandos de esta guía funcionan con Git instalado correctamente.

------------------------------------------------------------------------

## 6. Clonar el repositorio del grupo

La primera vez que trabajes con el proyecto deberás clonarlo.

El docente proporcionará la dirección del repositorio privado del grupo.

Ejemplo:

``` bash
git clone DIRECCION_DEL_REPOSITORIO
```

Luego entrá en la carpeta:

``` bash
cd p2-banco-tup13-g01
```

El repositorio se descarga con su historial y queda conectado al remoto
denominado normalmente `origin`.

Podés comprobarlo con:

``` bash
git remote -v
```

------------------------------------------------------------------------

## 7. Ver en qué rama estás

Utilizá:

``` bash
git branch
```

La rama actual aparecerá marcada con `*`.

También podés usar:

``` bash
git status
```

Al comenzar deberías estar en:

``` text
main
```

------------------------------------------------------------------------

## 8. Actualizar `main` antes de comenzar

Antes de crear una rama nueva, asegurate de tener la versión más
reciente.

``` bash
git switch main
git pull
```

Esto es especialmente importante a partir de la Iteración 2, porque
`main` contendrá la versión integrada de la semana anterior.

------------------------------------------------------------------------

## 9. Crear tu rama individual

Cada estudiante debe crear su propia rama desde `main`.

Formato:

``` text
iteracion-NN/nombre-apellido
```

Ejemplo:

``` bash
git switch -c iteracion-01/juan-perez
```

Comprobá:

``` bash
git branch
```

Deberías ver algo equivalente a:

``` text
* iteracion-01/juan-perez
  main
```

Desde este momento trabajás en tu rama.

------------------------------------------------------------------------

## 10. Publicar la rama por primera vez

Una rama creada localmente todavía no existe en GitHub.

La primera vez debés publicarla:

``` bash
git push -u origin iteracion-01/juan-perez
```

La opción `-u` vincula tu rama local con la rama remota.

Después de hacerlo una vez, normalmente alcanzará con:

``` bash
git push
```

------------------------------------------------------------------------

## 11. Trabajar en la iteración

En la Iteración 1, por ejemplo, cada estudiante creará su propio:

``` text
banco.py
```

Cada integrante debe escribir personalmente la solución completa.

No se divide el código de esta forma:

``` text
Alumno A → constructor
Alumno B → depositar
Alumno C → extraer
```

Todos deben resolver la iteración completa.

------------------------------------------------------------------------

## 12. `git status`: mirar antes de actuar

Uno de los comandos más importantes es:

``` bash
git status
```

Usalo frecuentemente.

Permite saber:

- qué archivos modificaste;
- qué archivos son nuevos;
- qué archivos están preparados para commit;
- en qué rama estás;
- si tenés commits pendientes de publicar.

Una buena costumbre es ejecutar:

``` bash
git status
```

antes de `git add`, antes de `git commit` y antes de cambiar de rama.

------------------------------------------------------------------------

## 13. `git add`: preparar cambios

Modificar un archivo no significa que automáticamente formará parte del
próximo commit.

Primero hay que agregarlo al área de preparación.

Para un archivo:

``` bash
git add banco.py
```

Para varios archivos específicos:

``` bash
git add banco.py README.md
```

También existe:

``` bash
git add .
```

pero al comenzar recomendamos agregar archivos de forma explícita para
comprender qué se está incorporando al commit.

Después:

``` bash
git status
```

------------------------------------------------------------------------

## 14. `git commit`: registrar una etapa

Un commit registra un estado significativo del trabajo.

Ejemplo:

``` bash
git commit -m "Agrega clase Cuenta"
```

Más adelante:

``` bash
git commit -m "Implementa deposito y extraccion"
```

Y después:

``` bash
git commit -m "Agrega pruebas de la iteracion 1"
```

No esperamos que el estudiante haga todo el trabajo y recién al final
genere un único commit.

Queremos observar la evolución del desarrollo.

Evitar mensajes como:

``` text
cambios
cosas
prueba
final
ultimo
```

Preferir mensajes que expliquen qué se hizo.

------------------------------------------------------------------------

## 15. `git push`: publicar los commits

Después de realizar commits:

``` bash
git push
```

Esto envía los commits de tu rama local a GitHub.

Durante la semana conviene publicar periódicamente.

No esperes al último momento para hacer el primer `push`.

------------------------------------------------------------------------

## 16. Ciclo normal de trabajo

Durante el desarrollo vas a repetir muchas veces:

``` bash
git status
git add banco.py
git commit -m "Describe el cambio realizado"
git push
```

Conceptualmente:

``` text
editar
  ↓
probar
  ↓
git status
  ↓
git add
  ↓
git commit
  ↓
git push
```

------------------------------------------------------------------------

## 17. No trabajar directamente sobre `main`

Los estudiantes no desarrollan las iteraciones directamente en `main`.

Antes de modificar código comprobá:

``` bash
git branch
```

o:

``` bash
git status
```

Si estás en:

``` text
main
```

y vas a comenzar una iteración, primero creá tu rama.

------------------------------------------------------------------------

## 18. ¿Qué es un Pull Request?

Un **Pull Request (PR)** es una propuesta para incorporar los cambios de
una rama en otra.

No significa simplemente "subir archivos".

Permite:

- comparar código;
- conversar sobre los cambios;
- hacer comentarios;
- solicitar correcciones;
- aprobar una propuesta;
- dejar registro de la revisión.

Los PR forman parte del trabajo evaluado del proyecto.

------------------------------------------------------------------------

## 19. Primer Pull Request: alumno → integración

Cuando hayas completado tu solución individual y publicado todos tus
commits, abrí GitHub y creá un Pull Request.

Para la Iteración 1 debe tener:

``` text
base:    integracion/iteracion-01
compare: iteracion-01/nombre-apellido
```

Prestá especial atención a `base`.

**No abras el PR individual directamente hacia `main`.**

El destino es:

``` text
integracion/iteracion-01
```

------------------------------------------------------------------------

## 20. Qué escribir en el Pull Request

Utilizá un título descriptivo.

Ejemplo:

``` text
Iteración 1 - Juan Pérez
```

En la descripción indicá brevemente:

- qué implementaste;
- qué pruebas realizaste;
- qué limitaciones observaste;
- cualquier decisión que quieras que el grupo revise.

No hace falta escribir un informe extenso.

------------------------------------------------------------------------

## 21. El líder de integración

Cada semana habrá un integrante que cumplirá el rol de líder.

El liderazgo será rotativo.

El líder deberá:

- verificar que los integrantes hayan presentado sus PR;
- revisar las propuestas;
- coordinar la comparación de soluciones;
- pedir cambios cuando corresponda;
- coordinar la construcción de la versión integrada;
- verificar que la solución grupal funcione;
- abrir el PR final hacia `main`.

El líder no debe programar por sus compañeros.

Tampoco debe elegir automáticamente su propia solución.

------------------------------------------------------------------------

## 22. Revisar un Pull Request

Los integrantes del grupo deben leer el código de sus compañeros.

Al revisar un PR pueden:

- realizar comentarios;
- hacer preguntas;
- señalar errores;
- proponer mejoras;
- aprobar;
- solicitar cambios.

La revisión debe centrarse en el código y en la consigna.

Ejemplos de comentarios útiles:

``` text
¿Podríamos evitar repetir esta operación?

Probé este caso y el resultado fue diferente al esperado.

Esta solución usa un concepto que todavía no vimos.

¿Podés explicar por qué elegiste este tipo de dato?
```

------------------------------------------------------------------------

## 23. Comparar antes de integrar

La rama de integración no debe convertirse simplemente en una copia de
la solución de un integrante.

Antes de integrar, el grupo debe comparar:

- nombres utilizados;
- estructura de la clase;
- métodos;
- pruebas;
- claridad;
- diferencias de diseño;
- errores encontrados;
- decisiones distintas.

El objetivo es construir una solución que todos puedan explicar.

------------------------------------------------------------------------

## 24. Rama de integración

Para cada semana existirá una rama:

``` text
integracion/iteracion-01
```

Luego:

``` text
integracion/iteracion-02
integracion/iteracion-03
...
```

Esta rama representa la propuesta final del grupo para esa iteración.

El líder coordina su construcción.

------------------------------------------------------------------------

## 25. Pull Request final: integración → `main`

Cuando el grupo considere terminada la iteración, el líder abre un
segundo PR:

``` text
base:    main
compare: integracion/iteracion-01
```

Este PR representa la entrega grupal.

El flujo completo queda:

``` text
iteracion-01/alumno-a ──┐
iteracion-01/alumno-b ──┤
iteracion-01/alumno-c ──┼── PR ──→ integracion/iteracion-01
iteracion-01/alumno-d ──┘                       │
                                               │ PR
                                               ↓
                                              main
```

El PR hacia `main` será revisado por la cátedra.

------------------------------------------------------------------------

## 26. `main` representa la versión aprobada

`main` no es una rama de experimentación.

Representa la versión integrada del proyecto aceptada hasta ese momento.

Por eso la Iteración 2 debe comenzar desde la versión actualizada de
`main`:

``` bash
git switch main
git pull
git switch -c iteracion-02/nombre-apellido
```

Así todos comienzan la nueva semana desde la misma base.

------------------------------------------------------------------------

## 27. Si el docente solicita cambios

Un PR no siempre será aprobado inmediatamente.

El docente puede solicitar modificaciones.

En ese caso, no hace falta abrir otro PR.

Se corrige en la misma rama:

``` bash
git switch integracion/iteracion-01
```

Se realizan los cambios y luego:

``` bash
git add .
git commit -m "Corrige observaciones de la revision"
git push
```

El Pull Request se actualiza automáticamente con los nuevos commits.

------------------------------------------------------------------------

## 28. Si un compañero solicita cambios

Lo mismo ocurre con un PR individual.

Si el líder o un compañero pide una corrección:

``` bash
git switch iteracion-01/nombre-apellido
```

Corregí el código:

``` bash
git add .
git commit -m "Corrige validacion solicitada en revision"
git push
```

El PR existente se actualizará.

No abras otro PR para la misma corrección.

------------------------------------------------------------------------

## 29. `git pull`: traer cambios del remoto

`git pull` descarga e integra los cambios de la rama remota
correspondiente.

Por ejemplo:

``` bash
git switch main
git pull
```

Antes de comenzar una nueva iteración es obligatorio actualizar `main`.

Si tenés cambios locales sin guardar, primero ejecutá:

``` bash
git status
```

No uses `git pull` mecánicamente sin saber qué modificaciones locales
tenés.

------------------------------------------------------------------------

## 30. Cambiar de rama

Para cambiar a una rama existente:

``` bash
git switch nombre-rama
```

Ejemplo:

``` bash
git switch main
```

o:

``` bash
git switch iteracion-01/juan-perez
```

Antes de cambiar de rama conviene:

``` bash
git status
```

y confirmar que el trabajo importante esté correctamente guardado.

------------------------------------------------------------------------

## 31. Ver las ramas

Ramas locales:

``` bash
git branch
```

Ramas locales y remotas:

``` bash
git branch -a
```

Actualizar la información de ramas remotas:

``` bash
git fetch
```

------------------------------------------------------------------------

## 32. Conflictos

Un conflicto puede aparecer cuando Git no puede decidir automáticamente
cómo combinar cambios.

No es un error excepcional: forma parte del trabajo colaborativo.

Cuando aparezca un conflicto:

1. no borres archivos al azar;
2. leé qué archivos informa Git;
3. abrí los archivos afectados;
4. identificá las diferencias;
5. decidí con el grupo qué versión conservar;
6. probá el programa;
7. agregá los archivos corregidos;
8. realizá el commit correspondiente.

Si no entendés el conflicto, consultá antes de ejecutar comandos
destructivos.

------------------------------------------------------------------------

## 33. Comandos que no deben usarse sin comprenderlos

Durante este proyecto evitá copiar de Internet comandos como:

``` text
git reset --hard
git push --force
git clean -fd
```

Pueden eliminar trabajo o modificar el historial.

Si Git muestra una situación que no sabés resolver, conservá el mensaje
de error y consultá.

------------------------------------------------------------------------

## 34. Qué no hacer

No trabajar toda la semana en `main`.

No compartir una única rama entre todos para desarrollar desde el
principio.

No hacer un solo commit al finalizar.

No reemplazar el trabajo propio copiando la rama de un compañero.

No abrir el PR individual directamente hacia `main`.

No hacer `push --force` para solucionar problemas sin comprender qué
hace.

No borrar el repositorio local porque apareció un conflicto.

No adelantar contenidos de próximas iteraciones solamente para que la
solución parezca más completa.

------------------------------------------------------------------------

## 35. Resumen de comandos para comenzar una iteración

``` bash
git switch main
git pull
git switch -c iteracion-01/nombre-apellido
git push -u origin iteracion-01/nombre-apellido
```

Durante el trabajo:

``` bash
git status
git add archivo.py
git commit -m "Describe el cambio realizado"
git push
```

Al terminar:

``` text
Abrir Pull Request en GitHub:

base:    integracion/iteracion-01
compare: iteracion-01/nombre-apellido
```

------------------------------------------------------------------------

## 36. Resumen del líder

El líder coordina:

``` text
PR individuales
      ↓
revisión y comparación
      ↓
integracion/iteracion-01
      ↓
pruebas grupales
      ↓
PR hacia main
      ↓
revisión docente
```

------------------------------------------------------------------------

## 37. Las cinco iteraciones

El mismo procedimiento se repite cada semana:

``` text
Iteración 1
iteracion-01/alumno
integracion/iteracion-01

Iteración 2
iteracion-02/alumno
integracion/iteracion-02

Iteración 3
iteracion-03/alumno
integracion/iteracion-03

Iteración 4
iteracion-04/alumno
integracion/iteracion-04

Iteración 5
iteracion-05/alumno
integracion/iteracion-05
```

Cada nueva iteración nace de la última versión aprobada de `main`.

------------------------------------------------------------------------

## 38. ¿Por qué trabajamos así?

En proyectos profesionales es frecuente dividir el trabajo por
funcionalidades.

Durante estas primeras cinco iteraciones utilizamos deliberadamente otra
estrategia.

Queremos que cada estudiante:

- programe todos los conceptos;
- enfrente personalmente los mismos problemas;
- construya una solución propia;
- pueda comparar decisiones;
- aprenda a leer código ajeno;
- aprenda a revisar;
- aprenda a integrar;
- pueda explicar el resultado final.

Más adelante podremos trabajar con ramas por funcionalidades, por
ejemplo:

``` text
feature/alta-cliente
feature/transferencias
feature/reportes
```

En ese momento el objetivo pedagógico será diferente: acercarnos a una
división de trabajo más parecida a la de un equipo profesional.

------------------------------------------------------------------------

## 39. Regla final

Git no se utilizará solamente para entregar archivos.

El historial del repositorio forma parte del proceso de aprendizaje.

Al finalizar cada iteración debe poder observarse:

``` text
cada estudiante desarrolló
        ↓
registró su evolución
        ↓
publicó su rama
        ↓
participó de un Pull Request
        ↓
revisó y comparó soluciones
        ↓
participó de la integración
        ↓
el grupo presentó una versión común
```

El objetivo no es solamente que el programa funcione.

El objetivo es que **todos puedan explicar cómo se construyó**.
