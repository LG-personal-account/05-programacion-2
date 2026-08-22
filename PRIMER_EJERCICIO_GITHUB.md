# Primer ejercicio de GitHub — Registro del grupo

## Objetivo

Esta será nuestra primera actividad utilizando GitHub.

El objetivo técnico es aprender a:

- editar un archivo alojado en GitHub;
- realizar un cambio;
- crear un commit;
- proponer una modificación;
- crear un Pull Request;
- esperar la revisión antes de incorporar el cambio.

El objetivo práctico es registrar los integrantes del grupo de trabajo que
utilizaremos posteriormente para el Proyecto Integrador.

---

## 1. Antes de comenzar

Cada estudiante debe tener su **propia cuenta de GitHub**.

Los grupos deben estar formados obligatoriamente por:

**3 o 4 estudiantes, ni menos ni más.**

Las comisiones son:

- **TUP11**
- **TUP13**

Antes de comenzar, el grupo debe tener definidos todos sus integrantes.

---

## 2. ¿Qué vamos a hacer?

En el repositorio general de Programación 2 existe un archivo llamado:

```text
GRUPOS.md
```

Uno de los integrantes del grupo deberá modificar ese archivo agregando los
datos de **todos los integrantes del grupo**.

El cambio no se incorporará directamente al repositorio.

Primero se enviará al docente mediante un **Pull Request**.

El procedimiento será:

```text
Abrir GRUPOS.md
       ↓
Editar el archivo
       ↓
Agregar nuestro grupo
       ↓
Guardar el cambio
       ↓
Crear un Pull Request
       ↓
Revisión docente
       ↓
Incorporación a main
```

---

## 3. Ingresar al repositorio

Ingresar al repositorio de **Programación 2** de la organización
`TUP-UTN-FRLP`.

El enlace será proporcionado por la cátedra.

Una vez dentro del repositorio, buscar el archivo:

```text
GRUPOS.md
```

y abrirlo.

---

## 4. Editar GRUPOS.md

Con `GRUPOS.md` abierto, buscar en la parte superior derecha del archivo el
ícono del lápiz:

```text
Edit this file
```

Hacer clic sobre él.

Si GitHub informa que no tenemos permiso para modificar directamente el
repositorio, es normal.

GitHub permitirá proponer el cambio mediante una copia propia del repositorio
(**fork**) y posteriormente enviar un **Pull Request**.

Seguir la opción que GitHub ofrece para proponer los cambios.

---

## 5. Buscar nuestra comisión

Dentro del archivo encontraremos secciones para:

```text
TUP11
```

y:

```text
TUP13
```

Debemos agregar nuestro grupo **únicamente dentro de la comisión a la que
pertenecemos**.

Antes de escribir, verificar:

- que ninguno de los integrantes ya figure en otro grupo;
- cuál es el último número de grupo utilizado en nuestra comisión.

Si el último grupo registrado es:

```text
TUP11 - Grupo 4
```

el nuevo grupo será:

```text
TUP11 - Grupo 5
```

---

## 6. Formato obligatorio

Agregar el grupo respetando el siguiente formato:

```text
**TUP11 - Grupo 1**

Integrantes:

PÉREZ Juan - 12345 - GitHub: juanperez
GONZÁLEZ Ana - 23456 - GitHub: anagonzalez
RODRÍGUEZ Pedro - 34567 - GitHub: pedrorodriguez
LÓPEZ María - 45678 - GitHub: marialopez
```

Los datos anteriores son solamente un ejemplo.

Cada grupo deberá reemplazarlos por:

```text
APELLIDO Nombre - Legajo - GitHub: usuario
```

Por ejemplo:

```text
**TUP13 - Grupo 3**

Integrantes:

FERNÁNDEZ Lucía - 15432 - GitHub: luciafernandez
MARTÍNEZ Pablo - 16543 - GitHub: pabloomartinez
SOSA Carla - 17654 - GitHub: carlasosa
```

Un grupo puede tener **3 o 4 integrantes**.

---

## 7. Verificar antes de guardar

Antes de continuar, revisar:

- comisión correcta;
- número de grupo correcto;
- 3 o 4 integrantes;
- apellido y nombre de cada integrante;
- legajo correcto;
- usuario de GitHub correcto;
- ningún integrante repetido en otro grupo;
- no haber modificado accidentalmente otro grupo.

**No modificar ni eliminar información correspondiente a otros grupos.**

---

## 8. Crear el commit

GitHub solicitará guardar o confirmar los cambios realizados.

Un **commit** es un registro de una modificación realizada en el proyecto.

Utilizar como mensaje:

```text
Registra TUP11 Grupo 1
```

reemplazando comisión y número según corresponda.

Por ejemplo:

```text
Registra TUP13 Grupo 4
```

Evitar mensajes como:

```text
cambio
```

```text
prueba
```

```text
grupo
```

El mensaje debe permitir entender qué se modificó.

---

## 9. Crear el Pull Request

Después de guardar el cambio, GitHub permitirá crear un:

```text
Pull Request
```

Un **Pull Request (PR)** es una propuesta para incorporar nuestros cambios al
repositorio principal.

En este caso estamos diciendo:

> Agregamos nuestro grupo a `GRUPOS.md` y solicitamos que el docente revise e
> incorpore el cambio.

Crear el Pull Request.

---

## 10. Título del Pull Request

Utilizar como título:

```text
Registro TUP11 - Grupo 1
```

Por ejemplo:

```text
Registro TUP13 - Grupo 3
```

---

## 11. Descripción del Pull Request

En la descripción escribir:

```text
Se solicita registrar el grupo indicado en GRUPOS.md.

Se verificaron los nombres, legajos y usuarios de GitHub de todos los
integrantes.
```

Luego crear el Pull Request.

---

## 12. ¿Qué ocurre ahora?

Una vez creado el Pull Request:

**no hay que hacer el merge.**

El docente revisará:

- comisión;
- cantidad de integrantes;
- integrantes repetidos;
- legajos;
- usuarios de GitHub;
- formato utilizado.

El PR puede tener distintos resultados.

### Si está correcto

El docente lo aprobará y lo incorporará a `main`.

### Si hay algo que corregir

El docente podrá escribir un comentario solicitando una modificación.

Por ejemplo:

```text
Falta indicar el usuario de GitHub de uno de los integrantes.
```

No crear otro Pull Request.

Se deberá corregir el existente.

---

## 13. ¿Qué significa hacer merge?

Durante esta actividad aparecerá por primera vez el concepto de:

```text
merge
```

Un merge significa **integrar los cambios propuestos a la rama principal**.

En este ejercicio:

```text
Cambio del estudiante
        ↓
Pull Request
        ↓
Revisión docente
        ↓
Merge
        ↓
main
```

El merge será realizado por el docente.

---

## 14. ¿Qué es main?

`main` es la rama principal del repositorio.

Podemos imaginarla como la versión oficial:

```text
Repositorio
    │
    └── main
         │
         ├── README.md
         ├── GRUPOS.md
         ├── METODOLOGIA_DE_TRABAJO.md
         └── MATERIAL/
```

Cuando el docente acepte nuestro Pull Request, los datos del grupo pasarán a
formar parte del `GRUPOS.md` oficial de `main`.

---

## 15. ¿Para qué necesitamos el usuario de GitHub?

Una vez registrados los grupos, la cátedra utilizará los usuarios de GitHub
para preparar los repositorios privados del **Proyecto Integrador Banco**.

Cada grupo tendrá posteriormente su propio repositorio privado.

Por ejemplo:

```text
p2-2026-banco-tup11-g01
p2-2026-banco-tup11-g02
p2-2026-banco-tup13-g01
```

Solamente los integrantes del grupo y los docentes autorizados tendrán acceso
a ese repositorio.

---

## 16. Qué aprendimos con este ejercicio

Aunque solamente hayamos modificado unas líneas de texto, ya habremos
utilizado por primera vez varios conceptos fundamentales de GitHub:

```text
Repositorio
     ↓
Archivo
     ↓
Modificación
     ↓
Commit
     ↓
Pull Request
     ↓
Revisión
     ↓
Merge
     ↓
main
```

Estos mismos conceptos serán utilizados posteriormente para trabajar con
código Python en el Proyecto Integrador.

---

## Checklist antes de enviar el Pull Request

Antes de terminar, comprobar:

- [ ] Mi grupo pertenece a TUP11 o TUP13.
- [ ] El grupo tiene 3 o 4 integrantes.
- [ ] Elegimos el número de grupo correcto.
- [ ] Escribimos apellido y nombre de todos.
- [ ] Indicamos el legajo de todos.
- [ ] Indicamos el usuario de GitHub de todos.
- [ ] Ningún integrante está registrado en otro grupo.
- [ ] No modificamos información de otros grupos.
- [ ] El commit tiene un mensaje descriptivo.
- [ ] Creamos el Pull Request.
- [ ] No hicimos el merge.

---

## Regla importante

En caso de duda, **no borrar, sobrescribir ni modificar el trabajo de otro
grupo**.

Realizar el Pull Request y utilizar los comentarios para consultar o responder
las observaciones del docente.

Este ejercicio es el primer paso para comenzar a trabajar de manera
colaborativa con Git y GitHub durante Programación 2.
