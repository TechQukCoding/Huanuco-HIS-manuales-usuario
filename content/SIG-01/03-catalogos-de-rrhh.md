# 3. Catálogos de Recursos Humanos

Cuatro catálogos de **Recursos Humanos** alimentan las fichas de empleados, la asistencia y las justificaciones. Funcionan como las listas de Mantenimiento (manual SIG-04, capítulo 2): indicadores, búsqueda, pestañas de estado y menú **Editar** / **Eliminar**.

## 3.1 Especialidades

Ruta: **Recursos Humanos › Especialidades**. Es la **cartera hospitalaria** organizada por especialidad principal. SIGARH la administra y el Panel Hospitalario usa **solo las opciones activas**.

<figure class="captura"><div class="marco"><img src="img/rrhh-especialidades.png" alt="Especialidades y subespecialidades" data-ruta="/sigarh/rrhh/especialidades" data-perfil="Personal de RR. HH. (datos de prueba)"></div>
<figcaption>Figura 3. Especialidades y subespecialidades.</figcaption></figure>

- **Indicadores:** Especialidades, Subespecialidades, En cartera, No activas y Asignaciones RR. HH. (médicos asignados).
- **Filtros:** Todas, **Sugeridas** (las que corresponden al nivel del hospital), En cartera y No activas, con el buscador *Buscar especialidad o subespecialidad*.
- Abra una especialidad para ver sus subespecialidades.

| Campo | Obligatorio | Descripción |
|---|:-:|---|
| Tipo | <span class="si">Sí</span> | **Especialidad** (principal de la cartera) o **Subespecialidad** (pertenece a una principal). |
| Especialidad principal | Solo subespecialidades | *Seleccione la especialidad principal*. |
| Nombre | <span class="si">Sí</span> | Nombre de la especialidad. |
| Código interno | <span class="no">No</span> | Ej.: ESP-LOCAL-01. |
| Descripción / notas | <span class="no">No</span> | Detalle. |

## 3.2 Días feriados

Ruta: **Recursos Humanos › Días Feriados**. Es el **calendario de fechas especiales** del hospital. Se usa para el cálculo de la asistencia y de los turnos.

- Elija el **año** y vea los feriados en dos vistas: **Calendario** (por meses) o **Lista**. Puede filtrar por mes (*Todos los meses*) y por estado.
- El indicador **Feriados activos en el año** cuenta los vigentes.

| Campo | Obligatorio | Descripción |
|---|:-:|---|
| Descripción | <span class="si">Sí</span> | Máximo 150 caracteres. Ej.: *Aniversario institucional*. |
| Fecha | <span class="si">Sí</span> | Al elegirla, el formulario muestra el día de la semana. |
| Tipo | <span class="no">No</span> | **Nacional** (todo el país), **Regional** (Región Huánuco) o **Local** (provincia o institución). |

!!! tip "Consejo"
    Cargue los feriados del año al comenzar enero: la asistencia y los turnos los toman en cuenta para todo el año.

## 3.3 Motivos de justificación

Ruta: **Recursos Humanos › Motivos de Justificación**. Catálogo de motivos para justificar ausencias del personal; se usa al registrar justificaciones, vacaciones y licencias (capítulos 5 a 7).

| Campo | Obligatorio | Descripción |
|---|:-:|---|
| Nombre | <span class="si">Sí</span> | Nombre del motivo. |
| Código | <span class="no">No</span> | Ayuda a agrupar en reportes. |
| Descripción | <span class="no">No</span> | Detalle. |
| Motivo activo | — | Los inactivos no se ofrecen al registrar. |

## 3.4 Tolerancias

Ruta: **Recursos Humanos › Tolerancias**. Define los **márgenes de tardanza permitidos** por dependencia y grupo ocupacional. Con ellas el sistema decide si una entrada cuenta o no como tardanza.

| Campo | Obligatorio | Descripción |
|---|:-:|---|
| Dependencia | <span class="si">Sí</span> | La dependencia a la que aplica. Debe ser la misma que se registra en la ficha del empleado. |
| Grupo ocupacional | <span class="si">Sí</span> | Grupo al que aplica. |
| Nombre de la regla | <span class="no">No</span> | Ej.: *Tolerancia médicos consulta externa*. Hasta 255 caracteres. |
| Tolerancia de entrada | <span class="no">No</span> | Minutos de margen tras la hora de entrada programada antes de marcar tardanza. |
| Tolerancia diaria acumulada | <span class="no">No</span> | Tope de minutos tolerados en el día para el grupo. |

Mientras llena el formulario, un panel lateral muestra el **Resumen** y un **Simulador**: escriba a cuántos minutos llega tarde un empleado y verá la **tardanza registrada**. Si llega dentro de la tolerancia, no cuenta como tardanza; si la supera, se descuentan los minutos de tolerancia.

!!! important "Importante"
    La tolerancia que se aplica a cada empleado sale de su **dependencia** y de su **grupo ocupacional** (campos de su ficha, capítulo 2). Si un empleado no tiene dependencia, no tendrá regla de tolerancia asociada.

La lista muestra Regla, Grupo ocupacional, **Tol. entrada**, **Tol. diaria** y Estado, con los indicadores *Reglas*, *Activas*, *Inactivas* y *Tolerancia media de entrada*.

## 3.5 Reglas de eliminación

| Catálogo | Regla | Mensaje |
|---|---|---|
| Especialidades | Las **oficiales** no se eliminan; se desactivan de la cartera del hospital. | *Las especialidades oficiales no se eliminan; puedes desactivarlas de la cartera del hospital.* |
| Especialidades | No se elimina una que tenga subespecialidades o esté asignada a empleados. | *No se puede eliminar: contiene N subespecialidad(es).* / *…está asignada a N empleado(s).* |
| Motivos de justificación | No se elimina un motivo ya usado. | *No se puede eliminar: el motivo se usa en N justificación(es).* |
