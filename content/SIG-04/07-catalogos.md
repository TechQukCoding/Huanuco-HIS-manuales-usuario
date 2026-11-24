# 7. Catálogos de Mantenimiento

Los catálogos son las listas de referencia que usan SIGARH y el HIS: de ellas salen los desplegables de las fichas de empleados, los roles de turno, las guardias y mucho más. Todos funcionan como se explica en el capítulo 2 y requieren el permiso **Administrar Mantenimiento** para crear o editar.

## 7.1 Orden recomendado de carga

Algunos catálogos dependen de otros. Cárguelos en este orden para no tener que volver atrás:

<div class="flujo">
<span class="paso ok">Grupos ocupacionales</span><span class="flecha">›</span>
<span class="paso ok">Profesiones</span><span class="flecha">›</span>
<span class="paso">Departamentos</span><span class="flecha">›</span>
<span class="paso">Servicios</span><span class="flecha">›</span>
<span class="paso">Dependencias</span>
</div>
<div class="flujo">
<span class="paso">Tipos de trabajador</span><span class="flecha">›</span>
<span class="paso">Niveles remunerativos</span><span class="flecha">›</span>
<span class="paso ko">Tipos de guardia</span><span class="flecha">›</span>
<span class="paso ko">Horarios</span><span class="flecha">›</span>
<span class="paso ko">Guardias valorizadas</span>
</div>
<div class="flujo">
<span class="paso">Tipos de actividad</span><span class="flecha">›</span>
<span class="paso">Actividades</span>
</div>

## 7.2 Campos comunes

La mayoría de los catálogos tienen **Nombre** (obligatorio), **Código** (opcional), una **Descripción** opcional y el interruptor **Activo**. Solo se describen aparte los campos propios de cada uno.

## 7.3 Estructura del hospital

### Departamentos

Áreas del hospital que agrupan servicios y personal. Columnas: **Departamento**, **Código**, **Estado**. Campos: Nombre (obligatorio), Código, Descripción, Activo.

### UPSS y servicios

Muestra la estructura asistencial del hospital como una jerarquía: abra una **UPSS** para ver sus **servicios** y, dentro de cada servicio, las **especialidades** que SIGARH comparte con la programación y la atención hospitalaria. Se busca por UPSS, servicio o especialidad.

| Campo del servicio | Obligatorio | Descripción |
|---|:-:|---|
| Nombre | <span class="si">Sí</span> | Nombre del servicio. |
| Código | <span class="no">No</span> | Código interno. |
| Departamento | <span class="no">No</span> | Departamento al que pertenece. |
| Piso | <span class="no">No</span> | Piso donde funciona (catálogo de Infraestructura hospitalaria). |
| Minutos por paciente (consulta externa) | <span class="no">No</span> | Define cuántos cupos abre cada bloque de rol aprobado. Vacío = **15 minutos**. |
| UPSS donde funciona el servicio | <span class="no">No</span> | Una o varias; se indica cuántas hay seleccionadas. |
| Especialidades atendidas | <span class="no">No</span> | Una o varias. |
| Descripción / Servicio activo | — | Los servicios inactivos no se pueden asignar. |

### Dependencias

Unidades administrativas y asistenciales. Columnas: Dependencia, Código, Clasificación, Departamento, Servicio, Estado.

| Campo | Obligatorio | Descripción |
|---|:-:|---|
| Nombre | <span class="si">Sí</span> | Nombre de la dependencia. |
| Código | <span class="no">No</span> | Código interno. |
| Clasificación | <span class="no">No</span> | **Administrativa** o **Asistencial**. |
| Departamento | <span class="no">No</span> | Se elige primero. |
| Servicio | <span class="no">No</span> | Solo se ofrecen los servicios del departamento elegido (*Elige primero el departamento*). Si no pertenece al departamento: *El servicio no pertenece al departamento seleccionado*. |
| Dependencia activa | — | Las inactivas no se pueden asignar. |

## 7.4 Personal

### Grupos ocupacionales

Clasifican al personal según su naturaleza ocupacional y **habilitan su categoría de rol de turno**.

| Campo | Descripción |
|---|---|
| Nombre y Código | Identifican al grupo. |
| Tipo de grupo | Clasificación del grupo; puede quedar en *Sin tipo*. |
| Categoría de rol de turno | Define a qué categoría de rol pertenece el personal del grupo: **Médicos**, **Otros profesionales de la salud**, **Residentes**, **Técnicos y auxiliares** o **Internos**. Solo el personal de este grupo podrá agregarse a un rol de esa categoría. La opción *Personal no clínico (no asignable a roles de turno)* lo excluye de los roles de turno. |

### Profesiones

Catálogo común del personal de salud con su grupo ocupacional. Columnas: Profesión, Grupo ocupacional, Colegio profesional, **Origen** y Estado.

| Campo | Obligatorio | Descripción |
|---|:-:|---|
| Nombre | <span class="si">Sí</span> | Nombre de la profesión. |
| Código interno | <span class="si">Sí</span> | Código corto. Algunas cuentas lo usan para validar al empleado (por ejemplo, el código de Médico Cirujano). |
| Grupo ocupacional | <span class="si">Sí</span> | Grupo al que pertenece. |
| Colegio profesional | <span class="no">No</span> | Colegio que la agrupa. |
| Categoría para roles de turno | <span class="no">No</span> | Determina en qué categoría aparece al crear roles de turno. |
| Profesión activa | — | Las inactivas no se pueden asignar. |

!!! note "Nota"
    Las **profesiones base** vienen con el sistema: conservan su denominación y clasificación y **no se eliminan**, solo se desactivan. En esta pantalla la opción Eliminar no está disponible.

### Tipos de trabajador

Modalidades de contratación del personal. Campos: Nombre (obligatorio), Código, **Categoría** del personal, Descripción y *Tipo activo* (*Se puede asignar en la ficha del empleado*).

### Niveles remunerativos

Niveles de remuneración que se asignan en la ficha del empleado. Campos: Nombre (obligatorio), Código, Descripción y Activo.

## 7.5 Guardias y actividades

### Tipos de guardia

| Campo | Obligatorio | Descripción |
|---|:-:|---|
| Nombre | <span class="si">Sí</span> | Nombre del tipo de guardia. |
| Código | <span class="no">No</span> | Código interno. |
| Horas | <span class="no">No</span> | Duración. |
| Guardia laborable | — | Apáguela para tipos **no laborables**: vacaciones, descanso, etc. |
| Requiere EPP | — | Apáguela cuando no aplique: guardia remota, descanso, etc. |
| Tipo activo | — | Disponible al programar guardias. |
| Descripción | <span class="no">No</span> | Detalle. |

Columnas de la lista: Nombre, Código, Horas, Laborable, EPP, Estado.

### Horarios de guardia

Franjas horarias que se asignan a turnos y guardias.

| Campo | Obligatorio | Descripción |
|---|:-:|---|
| Nombre | <span class="si">Sí</span> | Nombre de la franja. |
| Tipo de guardia | <span class="no">No</span> | Al elegirlo se completan la hora de fin y las horas totales. |
| Hora de inicio | <span class="si">Sí</span> | Inicio del turno. |
| Hora de fin | <span class="no">No</span> | Si es menor que la hora de inicio, el turno termina **al día siguiente**. |
| Horas totales | — | Se recalculan según inicio y fin. |
| Horario activo | — | Los inactivos no se pueden asignar. |

### Guardias valorizadas

Importe de cada tipo de guardia por grupo ocupacional y nivel remunerativo. Columnas: Tipo de guardia, Grupo ocupacional, Nivel remunerativo, Valor, Vigencia, Estado.

| Campo | Obligatorio | Descripción |
|---|:-:|---|
| Tipo de guardia | <span class="si">Sí</span> | Guardia que se valoriza. |
| Valor (S/) | <span class="si">Sí</span> | Importe en soles. |
| Grupo ocupacional | <span class="no">No</span> | Si se indica, la tarifa aplica a ese grupo. |
| Nivel remunerativo | <span class="no">No</span> | Si se indica, la tarifa aplica a ese nivel. |
| Vigente desde | <span class="si">Sí</span> | Fecha de inicio. |
| Vigente hasta | <span class="no">No</span> | Vacío = sigue vigente. |
| Sustento | <span class="si">Sí</span> | Documento o norma que respalda el importe. |
| Guardia activa | — | Las inactivas no se pueden asignar. |

**Qué tarifa se aplica.** Cuando hay varias, el sistema elige la más específica en este orden: **grupo y nivel**, solo **grupo**, solo **nivel**, y por último la **general**. Si no hay ninguna vigente, indica *No existe tarifa vigente*; si hay más de una igual de específica, *Hay tarifas ambiguas; revise las vigencias*.

!!! important "Importante"
    **Una tarifa cuya vigencia ya empezó no se modifica ni se elimina.** Para cambiar un importe: ciérrela con una fecha en **Vigente hasta** y cree una nueva tarifa. El sistema responde *La tarifa ya inició su vigencia; cierre su período y cree una nueva tarifa*, *No se puede cerrar una tarifa retroactivamente* o *Una tarifa con vigencia iniciada debe conservarse*.

### Tipos de actividad y Actividades

- **Tipos de actividad:** tipos de actividad complementaria del personal. Campos: Nombre (obligatorio), Código y Tipo activo (*Disponible al registrar actividades*).
- **Actividades:** actividades que el personal realiza en su rol de turno. Columnas: Actividad, Código, Tipo, Consultorio, Estado. Campos: Nombre (obligatorio), Código, **Tipo de actividad** y Actividad activa.
