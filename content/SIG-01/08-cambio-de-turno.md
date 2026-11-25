# 8. Cambio de turno

Un **cambio de turno** es el intercambio de turnos entre dos trabajadores: el **solicitante** pide que el **aceptante** cubra su **fecha original**, y el intercambio incluye una segunda fecha, la **fecha de reemplazo**.

## 8.1 Tramitar un cambio de turno

Ruta: **Movimientos › Cambio de Turno › Tramitar Cambio de Turno**. La pantalla se describe como *Solicitud entre dos trabajadores y dos fechas*.

<figure class="captura"><div class="marco"><img src="img/mov-cambio-turno-tramitar.png" alt="Tramitar cambio de turno" data-ruta="/sigarh/movimientos/cambio-turno/tramitar" data-perfil="Personal de RR. HH. (datos de prueba)"></div>
<figcaption>Figura 4. Tramitar cambio de turno.</figcaption></figure>

<ol class="pasos">
<li>Elija el <strong>Servicio</strong>.</li>
<li>Busque al <strong>solicitante</strong> por su <strong>DNI del solicitante</strong> y al <strong>aceptante</strong> por su <strong>DNI del aceptante</strong>.</li>
<li>Indique la <strong>Fecha original</strong> (el turno que se cede). No puede ser una fecha pasada.</li>
<li>Indique la <strong>Fecha de reemplazo</strong> (la segunda fecha del intercambio).</li>
<li>Escriba el <strong>N.° de documento</strong> de respaldo.</li>
<li>Pulse <strong>Tramitar cambio</strong>.</li>
</ol>

Reglas que aplica el sistema:

| Regla | Mensaje |
|---|---|
| El solicitante y el aceptante deben existir y estar activos. | *El solicitante no existe o no está activo* / *El aceptante no existe o no está activo* |
| No puede haber dos cambios pendientes o aprobados para el mismo solicitante y la misma fecha. | *Ya existe un cambio de turno pendiente o aprobado para ese solicitante y esa fecha* |

## 8.2 Revisar los cambios de turno

Ruta: **Movimientos › Cambio de Turno › Estado Cambio Turno** (*Revisa y decide las solicitudes de intercambio*).

- **Indicadores:** Solicitudes, Pendientes, Aprobados y Rechazados. Pestañas **Todos**, **Pendientes**, **Aprobados** y **Rechazados**.
- **Columnas:** Solicitud, Intercambio (solicitante y aceptante), Servicio, Fechas y Estado.
- **Acciones:** **Aprobar** y **Rechazar**. Al rechazar se abre *Rechazar cambio de turno* con el campo **Motivo del rechazo** (*Explica por qué se rechaza*).

### Qué ocurre al aprobar

- El cambio queda **Aprobado** y se registra quién lo revisó y cuándo.
- La **asistencia** del solicitante en la fecha original se marca con la nota *Cambio de turno: cubierto por …* y el nombre del aceptante.
- Si el solicitante tenía **programación médica activa** ese día, la agenda **se reasigna automáticamente** al aceptante, **siempre que el aceptante pertenezca al mismo servicio** de esa agenda.

!!! important "Importante"
    Si el aceptante no pertenece al servicio de la agenda, el sistema lo impide: *El aceptante no pertenece al servicio de la agenda que cubriría ese día; no se puede reasignar automáticamente la programación médica.* En ese caso, corrija el servicio del aceptante o resuelva la agenda manualmente antes de aprobar.

Un cambio ya decidido no se puede decidir otra vez: *El cambio de turno ya fue aprobado/rechazado*.
