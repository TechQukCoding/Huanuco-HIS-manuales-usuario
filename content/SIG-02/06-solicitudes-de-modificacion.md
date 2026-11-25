# 6. Solicitudes de modificación

Un rol **aprobado** no se edita. Para incorporar a una persona después de la aprobación se tramita una **solicitud de modificación**, que otra persona revisa.

<div class="flujo">
<span class="paso">Rol aprobado</span><span class="flecha">›</span>
<span class="paso ko">Solicitar incorporación</span><span class="flecha">›</span>
<span class="paso ok">Revisión en Roles Pendientes</span>
</div>

## 6.1 Solicitar una incorporación

Ruta: **Roles Aprobados › (rol) › Solicitar incorporación**. Se abre *Solicitud de incorporación de personal*.

<figure class="captura"><div class="marco"><img src="img/aprobados-solicitar.png" alt="Solicitud de incorporación de personal" data-ruta="/sigarh/roles-aprobados/[id]" data-perfil="Elaborador de roles (datos de prueba)"></div>
<figcaption>Figura 5. Solicitud de incorporación de personal.</figcaption></figure>

<ol class="pasos">
<li>Abra el rol aprobado y pulse <strong>Solicitar incorporación</strong>.</li>
<li>En <strong>Empleado a agregar</strong> pulse <em>Seleccionar empleado</em> y busque por nombre o DNI.</li>
<li>Escriba el <strong>Motivo de la modificación</strong> (<em>Sustento de la incorporación…</em>), de al menos 5 caracteres.</li>
<li>Opcional: en <strong>Programación propuesta</strong>, use <strong>Agregar actividad</strong>, elija el <strong>Turno</strong> (horario) y los días; use <strong>Quitar actividad</strong> o <strong>Quitar turno</strong> si se equivoca.</li>
<li>Pulse <strong>Enviar solicitud</strong>. Se envía a <em>Roles Pendientes › Solicitudes de modificación</em>.</li>
</ol>

Solo se puede solicitar sobre roles **aprobados**: *Solo se pueden solicitar modificaciones sobre roles aprobados.*

## 6.2 Revisar las solicitudes

Ruta: **Roles Pendientes › Solicitudes de Modificación** (*Incorporaciones de personal a roles ya aprobados*).

- **Indicadores y pestañas:** Todas, Pendientes, Aprobadas y Rechazadas.
- **Tabla:** Empleado propuesto, Rol, Solicitado por y Estado. El botón dice **Revisar** si está pendiente y **Ver** si ya se decidió.
- En la solicitud verá el **empleado propuesto**, la programación y el motivo. Pulse **Aprobar** o **Rechazar**.
- Al rechazar, escriba el **Motivo del rechazo** (mínimo 5 caracteres). *La solicitud se conserva en el historial con este motivo.*

| Regla | Mensaje |
|---|---|
| Debe tener el permiso de aprobación del servicio. | *No tiene permiso para aprobar modificaciones de roles de este servicio.* |
| **Quien solicitó no puede aprobar.** | *Quien solicitó la modificación no puede aprobarla; debe revisarla otra persona.* |
| El rol debe seguir aprobado. | *El rol asociado ya no está aprobado.* |
| El empleado no puede estar en otro rol ordinario del servicio y período. | *El empleado ya pertenece a otro rol ordinario de este servicio y período.* |
| Se vuelve a ejecutar el diagnóstico. | *No se puede aprobar la modificación: …* |
| Una solicitud se decide una sola vez. | *La solicitud ya fue revisada.* |

Al aprobar, el empleado se incorpora al rol, la agenda se sincroniza y se envía una notificación (*Solicitud de modificación aprobada*).
