# 4. Registro de asistencia

El **Registro de asistencia** es el control diario de entrada, salida y tardanzas del personal. Cada registro compara la jornada **programada** con la **real** (marcación) y calcula la tardanza usando la tolerancia que corresponde (capítulo 3).

Ruta: **SIGARH › Recursos Humanos › Registro de Asistencia**.

## 4.1 Listado

<figure class="captura"><div class="marco"><img src="img/rrhh-asistencia.png" alt="Registro de asistencia" data-ruta="/sigarh/rrhh/asistencia" data-perfil="Personal de RR. HH. (datos de prueba)"></div>
<figcaption>Figura 4. Registro de asistencia.</figcaption></figure>

<ol class="leyenda">
<li><strong>Registrar asistencia.</strong></li>
<li><strong>Indicadores.</strong> Registros, Con tardanza, Ausentes y Minutos de tardanza acumulados.</li>
<li><strong>Filtros.</strong> Empleado (<em>Todos los empleados</em>), <em>Día</em> o el rango <em>Desde</em> / <em>Hasta</em>, e interruptor <strong>Solo tardanzas</strong>. <strong>Limpiar filtros</strong> los quita.</li>
<li><strong>Tabla.</strong> Empleado, Fecha, Servicio / actividad, Programado, Real, H. trab. (horas trabajadas), Tardanza y Estado.</li>
</ol>

El menú de acciones de cada fila permite **Editar** (el empleado queda fijo y no se puede cambiar) o **Eliminar** el registro.

## 4.2 Registrar una asistencia

<ol class="pasos">
<li>Pulse <strong>Registrar asistencia</strong>.</li>
<li>Busque al <strong>Empleado</strong> por nombre y elija la <strong>Fecha</strong>. Si la fecha es feriado, el sistema avisa <em>Esta fecha es feriado</em>: el registro se permite igual y queda marcado.</li>
<li>Elija el <strong>Horario / guardia programada</strong>; las horas programadas se completan solas desde el horario. Indique, si lo necesita, el <strong>Servicio</strong> y la <strong>Actividad</strong>.</li>
<li>En <strong>Real (marcación)</strong> escriba la <strong>Entrada</strong> y la <strong>Salida</strong> reales.</li>
<li>Elija el <strong>Estado</strong> y, si desea, escriba una <strong>Observación</strong>.</li>
<li>Pulse el botón de registro (el sistema guarda el usuario que hace el registro).</li>
</ol>

| Campo | Obligatorio | Descripción |
|---|:-:|---|
| Empleado | <span class="si">Sí</span> | *El empleado es requerido*. En la edición queda fijo. |
| Fecha | <span class="si">Sí</span> | *La fecha es requerida*. |
| Grupo ocupacional | <span class="no">No</span> | Determina la regla de tolerancia. Se completa con el del empleado. |
| Horario / guardia programada | <span class="no">No</span> | Completa las horas programadas. |
| Servicio y Actividad | <span class="no">No</span> | Texto libre, hasta 100 caracteres. Ej.: *Emergencia* y *Guardia diurna*. |
| Programado: Entrada y Salida | <span class="no">No</span> | Hora de entrada y salida previstas. |
| Real: Entrada y Salida | <span class="no">No</span> | Marcación real. |
| Estado | <span class="no">No</span> | **Presente** (marcó a tiempo), **Tardanza** (llegó tarde), **Ausente** (no asistió) o **Justificado** (con justificación). |
| Observación | <span class="no">No</span> | Nota libre. |

## 4.3 Cómo se calcula la tardanza

- Si la entrada **real es posterior** a la programada, la tardanza son los minutos de diferencia **menos la tolerancia de entrada** que corresponde a la dependencia y al grupo del empleado. Si queda en cero o menos, no hay tardanza.
- Si hay tardanza calculada y el estado es **Presente**, el sistema lo cambia solo a **Tardanza**.
- Las **horas trabajadas** salen de la entrada y la salida reales. Si la salida es menor que la entrada, el sistema entiende que el turno **cruzó la medianoche**.
- Si la entrada real es más de 12 horas anterior a la programada, también se interpreta como cruce de medianoche (por ejemplo, programado 23:50 y real 00:10 son 20 minutos de tardanza).

!!! tip "Consejo"
    Mantenga al día los **feriados** y las **tolerancias** (capítulo 3): de ellos depende que la asistencia se calcule correctamente.

!!! note "Nota"
    Las justificaciones, vacaciones y licencias **aprobadas** marcan la asistencia del período como **Justificado** (capítulos 5 a 7).

