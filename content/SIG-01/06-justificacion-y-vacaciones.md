# 6. Justificación y vacaciones

La opción **Movimientos › Justificación y Vacaciones** es la **bandeja de revisión**: aquí se registran las solicitudes de vacaciones y de justificación, y se **aprueban o rechazan**.

<div class="flujo">
<span class="paso">Se registra la solicitud</span><span class="flecha">›</span>
<span class="paso ko">Pendiente</span><span class="flecha">›</span>
<span class="paso ok">Aprobada</span><span class="paso ko" style="margin-left:2mm">Rechazada</span>
</div>

## 6.1 Bandeja

<figure class="captura"><div class="marco"><img src="img/mov-justificacion-vacaciones.png" alt="Bandeja de justificación y vacaciones" data-ruta="/sigarh/movimientos/vacaciones" data-perfil="Jefatura o RR. HH. (datos de prueba)"></div>
<figcaption>Figura 2. Bandeja de justificación y vacaciones.</figcaption></figure>

- **Indicadores:** Solicitudes, Por revisar, Aprobadas, Rechazadas y Días aprobados.
- **Pestañas:** Todas, Pendientes, Aprobadas y Rechazadas. Además puede filtrar por **Motivo**.
- **Tabla:** Empleado (con DNI), Tipo (*Vacaciones* o *Justificación*), Período, Días, Motivo y Estado.
- **Acciones por fila:** **Aprobar**, **Rechazar** y, en el menú **Más acciones**, **Ver detalle**, **Abrir ficha** (del empleado) y **Ver documento** (el enlace sustentatorio).

## 6.2 Registrar una solicitud

<ol class="pasos">
<li>Pulse <strong>Nueva solicitud</strong> (<em>Justificación / inasistencia o solicitud de vacaciones</em>).</li>
<li>Elija el <strong>Tipo de movimiento</strong>: <strong>Justificación / inasistencia</strong> (ausencia o permiso con sustento) o <strong>Vacaciones</strong> (descanso vacacional).</li>
<li>Busque al trabajador por su <strong>DNI</strong>. Se busca en el registro de Empleados; si no existe, el sistema indica <em>No se encontró un empleado con DNI …</em>.</li>
<li>Complete motivo, N.° de documento, fecha de trámite y el período (<strong>Desde</strong> y <strong>Hasta</strong>).</li>
<li>Adjunte, si lo tiene, el <strong>enlace del documento sustentatorio</strong> y escriba el <strong>Detalle</strong> (hasta 500 caracteres).</li>
<li>Pulse <strong>Registrar solicitud</strong>. Queda en estado <strong>Pendiente</strong>.</li>
</ol>

!!! note "Nota"
    Los días se cuentan desde la fecha de inicio hasta la de fin, **ambas incluidas**. No se descuentan feriados ni fines de semana.

## 6.3 Aprobar o rechazar

1. Ubique la solicitud en la bandeja (pestaña **Pendientes**).
2. Pulse **Aprobar**, o **Rechazar**.
3. Si rechaza, se abre **Rechazar solicitud** con el campo **Motivo del rechazo**: escriba la razón y confirme.

Con **Ver detalle** se abre un panel con el tipo, los días, el motivo y, si fue rechazada, el **motivo del rechazo**.

!!! important "Importante"
    **Al aprobar unas vacaciones, el sistema retira de la agenda de Consulta Externa los cupos del período y marca en riesgo las citas ya tomadas.** Avise al servicio antes de aprobar si el empleado es un médico con agenda.

Una solicitud ya decidida no se puede decidir de nuevo (*La solicitud ya fue …, no puede volver a decidirse*). El resultado se notifica en las **Notificaciones** de SIGARH.

!!! note "Nota"
    Justificaciones, vacaciones y licencias comparten el mismo registro, pero cada **tipo** depende de su propio submódulo. Su perfil solo puede registrar y revisar los tipos que tenga asignados; si intenta otro, el sistema responde *No tiene permiso para asignar este tipo de solicitud.*
