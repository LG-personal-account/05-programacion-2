# Guía de Git y GitHub para el Proyecto Integrador

Esta guía está pensada para estudiantes que comienzan a trabajar con
**Git y GitHub** y necesitan participar en el Proyecto Integrador de
Programación 2.

El objetivo no es aprender todos los comandos de Git, sino dominar el flujo
mínimo necesario para trabajar correctamente en equipo utilizando
**feature branches** y **Pull Requests**.

---

## 1. Qué son Git y GitHub

**Git** es un sistema de control de versiones.

Permite registrar la evolución de un proyecto y conservar un historial de
los cambios realizados.

**GitHub** es un servicio en Internet que permite alojar repositorios Git y
trabajar de manera colaborativa.

Durante el proyecto existirán dos copias principales del repositorio:

```text
Repositorio local
Tu computadora
      │
      │ git push
      ↓
Repositorio remoto
GitHub
```

Y en sentido contrario:

```text
GitHub
Repositorio remoto
      │
      │ git pull
      ↓
Tu computadora
Repositorio local
```

En esta materia llamaremos normalmente:

- **local**: al repositorio que está en nuestra computadora;
- **remoto**: al repositorio alojado en GitHub;
- **origin**: al nombre que Git suele asignar al repositorio remoto principal.

---

## 2. Cada estudiante debe usar su propia cuenta

Cada integrante debe trabajar utilizando **su propia cuenta de GitHub**.

No se deben compartir cuentas entre integrantes.

Esto es importante porque GitHub y Git permiten registrar quién realizó cada
cambio y observar la participación individual dentro del trabajo grupal.

---

## 3. Organización recomendada en la computadora

Conviene crear una carpeta general para las materias y proyectos de la
TECNICATURA.

Por ejemplo:

```text
TUP/
└── programacion-2/
    └── proyectos/
        └── banco-grupo-01/
```

En Windows puede estar, por ejemplo, dentro de `Documentos`.

Se recomienda evitar, cuando sea posible:

- nombres de carpetas excesivamente largos;
- caracteres extraños;
- trabajar sobre una carpeta compartida entre integrantes;
- copiar el proyecto mediante unidad USB, ZIP, Google Drive o WhatsApp;
- colocar el repositorio dentro de una carpeta sincronizada que pueda generar
  conflictos automáticos.

La sincronización del proyecto entre integrantes se realizará mediante
**Git y GitHub**.

---

## 4. Abrir una terminal Bash en Visual Studio Code

Abrir Visual Studio Code y seleccionar:

```text
Terminal → New Terminal
```

Si Git Bash está instalado pero VS Code abrió PowerShell, se puede seleccionar
el tipo de terminal desde el menú de la terminal y elegir:

```text
Git Bash
```

Para comprobar que Git está instalado:

```bash
git --version
```

Deberá mostrarse una versión de Git.

---

## 5. Configuración inicial de Git

Esta configuración se realiza normalmente **una sola vez por computadora**.

Configurar el nombre:

```bash
git config --global user.name "Nombre Apellido"
```

Configurar el correo:

```bash
git config --global user.email "correo@ejemplo.com"
```

Se recomienda utilizar el mismo correo asociado a la cuenta de GitHub.

Para comprobar la configuración:

```bash
git config --global user.name
git config --global user.email
```

---

## 6. El repositorio del grupo ya estará creado

Para el Proyecto Integrador, la cátedra creará un repositorio privado para
cada grupo.

Por ejemplo:

```text
p2-2026-banco-tup11-g01
```

o:

```text
p2-2026-banco-tup13-g03
```

Cada grupo deberá utilizar **únicamente el repositorio que le fue asignado**.

Los integrantes del grupo tendrán acceso a ese repositorio y no a los
repositorios privados de los demás grupos.

---

## 7. Primera descarga del proyecto: `git clone`

Cuando el repositorio ya existe en GitHub, **NO se debe ejecutar `git init`**.

Se utiliza:

```bash
git clone URL_DEL_REPOSITORIO
```

Por ejemplo:

```bash
git clone https://github.com/ORGANIZACION/p2-2026-banco-tup11-g01.git
```

`git clone`:

- descarga el repositorio;
- crea la carpeta local;
- copia el historial existente;
- configura automáticamente el repositorio remoto;
- normalmente denomina `origin` a ese remoto.

Después ingresar a la carpeta:

```bash
cd p2-2026-banco-tup11-g01
```

Y abrirla en VS Code:

```bash
code .
```

---

## 8. Comprobar el repositorio remoto

Para comprobar a qué repositorio de GitHub está conectado el proyecto:

```bash
git remote -v
```

Se verá algo parecido a:

```text
origin  https://github.com/ORGANIZACION/proyecto.git (fetch)
origin  https://github.com/ORGANIZACION/proyecto.git (push)
```

`origin` es simplemente el nombre que tiene el repositorio remoto dentro de
la configuración local.

---

## 9. El comando que deben usar permanentemente: `git status`

Antes y después de casi cualquier operación conviene ejecutar:

```bash
git status
```

Este comando informa, entre otras cosas:

- en qué rama estamos;
- qué archivos fueron modificados;
- qué archivos son nuevos;
- qué archivos fueron eliminados;
- qué cambios están preparados para un commit;
- qué cambios todavía no fueron preparados.

Ante una duda, el primer comando debería ser:

```bash
git status
```

---

## 10. Qué es un commit

Un **commit** es un registro de un conjunto de cambios realizados en el
proyecto.

Puede pensarse como una fotografía identificada del estado del proyecto en
un momento determinado.

Ejemplos de buenos mensajes de commit:

```text
Agrega clase Titular
```

```text
Implementa creación de cuentas
```

```text
Valida saldo antes de realizar extracción
```

```text
Corrige transferencia entre cuentas
```

Evitar mensajes como:

```text
cambios
```

```text
cosas
```

```text
prueba
```

```text
final
```

El historial debe permitir comprender cómo fue evolucionando el programa.

---

## 11. Qué hace `git add`

Modificar un archivo **no significa que automáticamente formará parte del
próximo commit**.

Git permite elegir qué cambios queremos incluir.

Supongamos que modificamos:

```text
titular.py
cuenta.py
```

Para preparar solamente `titular.py`:

```bash
git add titular.py
```

Para preparar ambos:

```bash
git add titular.py cuenta.py
```

Para preparar todos los cambios de la carpeta actual:

```bash
git add .
```

Luego comprobar:

```bash
git status
```

Los archivos preparados aparecerán dentro de los cambios que serán incluidos
en el próximo commit.

### Recomendación

Para principiantes es preferible acostumbrarse a mirar primero:

```bash
git status
```

y agregar conscientemente los archivos que corresponden.

`git add .` es cómodo, pero puede incorporar archivos que no pretendíamos
subir.

---

## 12. Crear el commit

Después de realizar `git add`, crear el commit:

```bash
git commit -m "Agrega clase Titular"
```

El mensaje debe describir brevemente qué cambio se realizó.

Un commit queda guardado inicialmente en el **repositorio local**.

Todavía no está necesariamente en GitHub.

---

## 13. Qué hace `git push`

`git push` envía al repositorio remoto los commits realizados localmente.

Es decir:

```text
PC
commits locales
      │
      │ git push
      ↓
GitHub
```

En una rama que ya está vinculada con GitHub normalmente alcanza con:

```bash
git push
```

La primera vez que se publica una nueva rama utilizaremos:

```bash
git push -u origin nombre-de-la-rama
```

La opción `-u` deja vinculada la rama local con su correspondiente rama
remota.

Después de eso, normalmente bastará con:

```bash
git push
```

---

## 14. Qué hace `git pull`

`git pull` trae cambios desde GitHub e intenta integrarlos en la rama local
actual.

```text
GitHub
      │
      │ git pull
      ↓
PC
```

Antes de comenzar a trabajar sobre una rama compartida o sobre `main`,
conviene asegurarse de tener la versión actualizada.

Por ejemplo:

```bash
git switch main
git pull
```

---

## Trabajo con ramas

## 15. Qué es una branch

Una **branch** o **rama** permite desarrollar una parte del programa de forma
separada.

La rama principal del proyecto será:

```text
main
```

`main` representa la versión integrada del programa.

Para desarrollar una nueva funcionalidad se creará otra rama.

Por ejemplo:

```text
main
│
├── feature/alta-titular
├── feature/crear-cuenta
├── feature/depositar
├── feature/extraer
└── feature/transferencia
```

La idea es:

```text
main
  │
  └── feature/crear-cuenta
               │
               ├── trabajo
               ├── commits
               └── pruebas
```

Cuando la funcionalidad está terminada se propone incorporarla nuevamente a
`main`.

---

## 16. Las ramas representan tareas, no personas

No utilizar ramas permanentes como:

```text
juan
ana
pedro
rama-juan
rama-ana
```

Se utilizarán nombres asociados a funcionalidades:

```text
feature/alta-titular
feature/crear-cuenta
feature/listar-cuentas
feature/transferencia
fix/validar-saldo
```

Esto permite saber qué objetivo tiene cada rama independientemente de quién
la esté desarrollando.

---

## 17. Antes de crear una feature branch

Primero ubicarse en `main`:

```bash
git switch main
```

Actualizarla:

```bash
git pull
```

Comprobar:

```bash
git status
```

La rama nueva deberá nacer desde una versión actualizada de `main`.

---

## 18. Crear una feature branch

Ejemplo:

```bash
git switch -c feature/alta-titular
```

`-c` significa que se crea una nueva rama y se cambia inmediatamente a ella.

Comprobar:

```bash
git branch
```

Se verá algo parecido a:

```text
* feature/alta-titular
  main
```

El `*` indica la rama en la que estamos trabajando.

También puede comprobarse con:

```bash
git status
```

---

## 19. Flujo normal de trabajo dentro de una feature

Supongamos que estamos trabajando en:

```text
feature/alta-titular
```

Modificar los archivos necesarios.

Después:

```bash
git status
```

Preparar los cambios:

```bash
git add titular.py
```

Crear el commit:

```bash
git commit -m "Implementa alta de titular"
```

Publicar la rama por primera vez:

```bash
git push -u origin feature/alta-titular
```

A partir de allí, los siguientes avances pueden publicarse con:

```bash
git push
```

---

## 20. No esperar hasta el final para hacer commits

No se recomienda trabajar varios días y realizar un único commit al terminar.

Es preferible:

```text
Implementa constructor de Titular
Agrega validación de DNI
Agrega método para mostrar titular
Corrige validación de nombre vacío
```

que:

```text
Proyecto terminado
```

Los commits frecuentes:

- reducen el riesgo de perder trabajo;
- permiten entender cómo evolucionó una funcionalidad;
- facilitan detectar errores;
- ayudan al trabajo colaborativo;
- permiten realizar seguimiento del proceso.

---

## Pull Requests

## 21. Qué es un Pull Request

Un **Pull Request**, normalmente abreviado **PR**, es una propuesta para
incorporar los cambios de una rama dentro de otra.

En este proyecto, normalmente será:

```text
feature/alta-titular
          │
          │ Pull Request
          ↓
         main
```

Un PR **no es simplemente entregar código**.

Permite:

- mostrar qué se modificó;
- revisar archivos;
- realizar comentarios;
- solicitar correcciones;
- discutir decisiones;
- aprobar la integración;
- finalmente unir los cambios a `main`.

---

## 22. Crear un Pull Request

Antes de crear el PR asegurarse de haber publicado todos los commits:

```bash
git status
git push
```

Luego ingresar al repositorio del grupo en GitHub.

GitHub normalmente mostrará la rama recientemente publicada y ofrecerá:

```text
Compare & pull request
```

También puede hacerse desde:

```text
Pull requests → New pull request
```

Seleccionar:

```text
base: main
compare: feature/alta-titular
```

Esto significa:

```text
Quiero incorporar:
feature/alta-titular

dentro de:
main
```

---

## 23. Título y descripción del PR

El título debe explicar qué funcionalidad se incorpora.

Ejemplo:

```text
Implementa alta de titulares
```

En la descripción indicar brevemente:

```text
- Se agrega la clase Titular.
- Se validan nombre y DNI.
- Se incorpora el alta desde el menú.
- Se probaron altas válidas e inválidas.
```

No utilizar títulos como:

```text
cambios
```

o:

```text
mi parte
```

---

## 24. Revisar un Pull Request de un compañero

El código grupal debe ser conocido por el grupo.

No alcanza con que cada integrante conozca solamente "su parte".

Cuando un compañero abre un PR, los demás integrantes deben poder revisar los
cambios.

En GitHub entrar al Pull Request.

Las pestañas principales permiten observar:

```text
Conversation
Commits
Files changed
```

En **Files changed** puede revisarse exactamente qué líneas se agregaron,
modificaron o eliminaron.

---

## 25. Comentar un Pull Request

Durante la revisión pueden realizarse comentarios generales o comentarios
sobre líneas específicas.

Por ejemplo:

```text
¿Podemos validar aquí que el DNI no esté vacío?
```

```text
Este método parece estar haciendo dos tareas diferentes.
```

```text
¿Probamos qué ocurre cuando el saldo es insuficiente?
```

Los comentarios deben referirse al código y ayudar a mejorar la solución.

El objetivo de una revisión no es señalar quién "se equivocó", sino detectar
problemas antes de integrar los cambios.

---

## 26. Responder a observaciones de un PR

Supongamos que se abrió:

```text
feature/alta-titular → main
```

y durante la revisión se solicita corregir una validación.

No es necesario crear otro Pull Request.

Volver a la misma rama local:

```bash
git switch feature/alta-titular
```

Realizar la corrección.

Después:

```bash
git status
git add titular.py
git commit -m "Corrige validación de DNI"
git push
```

El Pull Request existente se actualizará automáticamente con el nuevo commit.

Luego puede responderse al comentario indicando que la corrección fue
realizada.

---

## 27. Aprobar o solicitar cambios

Cuando se revisa un Pull Request, GitHub permite realizar una revisión.

Según los permisos y configuración del repositorio pueden aparecer opciones
como:

```text
Comment
Approve
Request changes
```

### Comment

Realiza observaciones sin aprobar ni rechazar formalmente.

### Approve

Indica que los cambios fueron revisados y pueden integrarse.

### Request changes

Indica que deben realizarse modificaciones antes de integrar el PR.

---

## 28. Cuándo hacer el merge

El **merge** incorpora los cambios de la feature branch dentro de `main`.

```text
feature/alta-titular
          │
          ↓
        merge
          │
          ↓
         main
```

No realizar el merge mientras existan correcciones importantes pendientes.

Como regla de trabajo:

1. terminar la funcionalidad;
2. publicar los cambios;
3. abrir el Pull Request;
4. revisar el código;
5. responder observaciones;
6. corregir si es necesario;
7. aprobar;
8. integrar a `main`.

Si la cátedra establece que determinados PR deben ser revisados por un
docente antes del merge, se deberá esperar esa revisión.

---

## Mantener el proyecto actualizado

## 29. Después de que un PR fue integrado

Cuando una funcionalidad fue incorporada a `main`, actualizar el repositorio
local:

```bash
git switch main
git pull
```

Ahora `main` local tendrá los cambios que fueron integrados en GitHub.

---

## 30. Comenzar una nueva funcionalidad

Siempre comenzar desde `main` actualizada:

```bash
git switch main
git pull
git switch -c feature/nueva-funcionalidad
```

Por ejemplo:

```bash
git switch main
git pull
git switch -c feature/crear-cuenta
```

---

## 31. Si `main` cambió mientras trabajábamos

Puede ocurrir que otro integrante haya integrado una funcionalidad mientras
nosotros todavía estamos trabajando.

Una forma sencilla de incorporar esos cambios a nuestra rama es:

```bash
git switch main
git pull
git switch feature/mi-funcionalidad
git merge main
```

Si no existen conflictos, Git integrará los cambios.

Si existen conflictos, deberán resolverse antes de continuar.

---

## Conflictos

## 32. Qué es un conflicto

Un conflicto puede aparecer cuando dos ramas modificaron partes incompatibles
del mismo archivo.

Git no decide automáticamente cuál versión debe conservarse porque necesita
una decisión humana.

Visual Studio Code mostrará las zonas en conflicto.

Pueden aparecer marcas similares a:

```text
código de nuestra rama
```

No se deben dejar estas marcas en el archivo final.

El grupo debe decidir qué código corresponde conservar o cómo combinar ambas
versiones.

---

## 33. Después de resolver un conflicto

Guardar el archivo corregido.

Luego:

```bash
git status
```

Preparar el archivo:

```bash
git add archivo.py
```

Finalizar el merge:

```bash
git commit
```

Y publicar:

```bash
git push
```

Ante un conflicto que no se comprenda, es preferible **detenerse y consultar**
antes de comenzar a ejecutar comandos encontrados al azar en Internet.

---

## Comandos útiles

## 34. Ver las ramas

```bash
git branch
```

La rama actual aparece marcada con `*`.

Para ver también ramas remotas:

```bash
git branch -a
```

---

## 35. Cambiar de rama

```bash
git switch nombre-rama
```

Ejemplo:

```bash
git switch main
```

---

## 36. Crear una rama y cambiar a ella

```bash
git switch -c nombre-rama
```

Ejemplo:

```bash
git switch -c feature/transferencia
```

---

## 37. Ver el historial

```bash
git log --pretty=format:'%h %s'
```

Ejemplo:

```text
8ad09fb Corrige validación de saldo
31ac140 Implementa extracción
a423190 Agrega clase Cuenta
```

Para salir de la vista del historial presionar:

```text
q
```

---

## 38. Ver cambios antes del `git add`

```bash
git diff
```

Permite revisar qué se modificó antes de preparar los archivos.

---

## 39. Ver cambios que ya fueron agregados

```bash
git diff --staged
```

Permite revisar qué cambios entrarían en el próximo commit.

---

## Flujo completo recomendado

## 40. Inicio de una nueva tarea

```bash
git switch main
git pull
git switch -c feature/nombre-de-la-tarea
```

---

## 41. Durante el desarrollo

Modificar código y repetir cuando sea necesario:

```bash
git status
git add archivo.py
git commit -m "Describe el cambio realizado"
```

---

## 42. Publicar la feature branch por primera vez

```bash
git push -u origin feature/nombre-de-la-tarea
```

Después de nuevos commits:

```bash
git push
```

---

## 43. Crear el Pull Request

En GitHub:

```text
feature/nombre-de-la-tarea
              ↓
        Pull Request
              ↓
             main
```

Revisar:

- título;
- descripción;
- archivos modificados;
- commits incluidos;
- que la rama base sea `main`.

---

## 44. Si el PR requiere correcciones

Continuar trabajando sobre **la misma rama**:

```bash
git switch feature/nombre-de-la-tarea
```

Modificar.

Después:

```bash
git add archivo.py
git commit -m "Corrige observaciones del PR"
git push
```

El PR se actualiza automáticamente.

---

## 45. Después del merge

Actualizar `main`:

```bash
git switch main
git pull
```

La feature branch ya cumplió su función.

Se puede eliminar localmente:

```bash
git branch -d feature/nombre-de-la-tarea
```

En GitHub también puede utilizarse **Delete branch** después del merge.

---

## Ejemplo completo

## 46. Ana desarrolla el alta de titulares

Primero actualiza `main`:

```bash
git switch main
git pull
```

Crea su feature:

```bash
git switch -c feature/alta-titular
```

Trabaja sobre:

```text
titular.py
```

Comprueba:

```bash
git status
```

Agrega:

```bash
git add titular.py
```

Crea un commit:

```bash
git commit -m "Agrega clase Titular"
```

Continúa trabajando y crea otro commit:

```bash
git add titular.py
git commit -m "Agrega validaciones de Titular"
```

Publica la rama:

```bash
git push -u origin feature/alta-titular
```

Luego abre en GitHub:

```text
feature/alta-titular → main
```

mediante un Pull Request.

Juan revisa el PR y solicita validar que el DNI no sea vacío.

Ana corrige el archivo y ejecuta:

```bash
git add titular.py
git commit -m "Valida DNI obligatorio"
git push
```

El Pull Request se actualiza automáticamente.

Luego de la revisión y aprobación, la rama se integra a `main`.

Finalmente Ana actualiza su copia local:

```bash
git switch main
git pull
```

---

## Reglas de trabajo para el Proyecto Integrador

## 47. Reglas básicas

Durante el Proyecto Integrador:

1. Cada estudiante utilizará su propia cuenta de GitHub.
2. Cada grupo trabajará únicamente en su repositorio asignado.
3. `main` representa la versión integrada del proyecto.
4. Las nuevas funcionalidades se desarrollarán en feature branches.
5. Las ramas se nombrarán por tarea o funcionalidad.
6. Se realizarán commits pequeños y descriptivos.
7. Los avances se publicarán regularmente con `git push`.
8. La integración de una feature a `main` se realizará mediante Pull Request.
9. Los integrantes revisarán el código de sus compañeros.
10. Las correcciones solicitadas en un PR se realizarán sobre la misma rama.
11. Antes de iniciar una nueva feature se actualizará `main`.
12. No se compartirán proyectos mediante ZIP, memoria USB o carpetas compartidas.
13. No se utilizará `git push --force` salvo indicación expresa del docente.
14. No se borrará la carpeta `.git`.
15. No se ejecutará `git init` dentro de un repositorio que fue clonado.

---

## Errores frecuentes

## 48. "Modifiqué archivos pero Git no los subió"

Revisar:

```bash
git status
```

Probablemente falte:

```bash
git add archivo.py
git commit -m "Mensaje"
git push
```

---

## 49. "Hice commit pero no aparece en GitHub"

El commit está probablemente solo en el repositorio local.

Ejecutar:

```bash
git push
```

---

## 50. "GitHub tiene cambios que yo no tengo"

Actualizar la rama correspondiente:

```bash
git pull
```

En `main`:

```bash
git switch main
git pull
```

---

## 51. "No sé en qué rama estoy"

Ejecutar:

```bash
git status
```

o:

```bash
git branch
```

---

## 52. "Empecé a programar y estaba en `main`"

No continuar agregando más cambios sin revisar la situación.

Ejecutar:

```bash
git status
```

y consultar al grupo o al docente antes de intentar corregirlo con comandos
que puedan perder trabajo.

---

## 53. "Tengo un conflicto"

No borrar archivos ni ejecutar comandos al azar.

Primero:

```bash
git status
```

Revisar los archivos indicados como conflictivos, resolverlos conscientemente
y consultar si no se comprende qué versión debe conservarse.

---

## Guía rápida

## Antes de comenzar una tarea

```bash
git switch main
git pull
git switch -c feature/nombre-tarea
```

## Mientras trabajo

```bash
git status
git add archivo.py
git commit -m "Descripción clara"
git push
```

La primera vez que publico la rama:

```bash
git push -u origin feature/nombre-tarea
```

## Cuando termino la funcionalidad

```text
GitHub
→ Pull requests
→ New pull request
→ base: main
→ compare: feature/nombre-tarea
```

## Si me piden correcciones

```bash
git switch feature/nombre-tarea
git add archivo.py
git commit -m "Corrige observaciones del PR"
git push
```

## Después de integrar el PR

```bash
git switch main
git pull
git branch -d feature/nombre-tarea
```

---

## Idea central

El flujo de trabajo que utilizaremos puede resumirse así:

```text
main actualizada
      │
      ↓
feature branch
      │
      ↓
desarrollo
      │
      ↓
git add
      │
      ↓
git commit
      │
      ↓
git push
      │
      ↓
Pull Request
      │
      ↓
revisión
      │
      ↓
correcciones
      │
      ↓
aprobación
      │
      ↓
merge
      │
      ↓
main
```

El objetivo no es solamente aprender comandos.

El objetivo es aprender a construir software de manera **progresiva,
ordenada, trazable y colaborativa**.
