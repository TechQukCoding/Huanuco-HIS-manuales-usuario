# 3. Programar el rol

El editor del rol guía la programación en **cinco pasos**, que se marcan al completarse y alimentan una barra de progreso:

<div class="flujo">
<span class="paso ok">Ámbito y período</span><span class="flecha">›</span>
<span class="paso ok">Personal</span><span class="flecha">›</span>
<span class="paso ok">Actividades</span><span class="flecha">›</span>
<span class="paso">Turnos</span><span class="flecha">›</span>
<span class="paso ko">Envío a revisión</span>
</div>

<figure class="captura"><div class="marco"><img src="img/roles-editor.png" alt="Editor de un rol de turno" data-ruta="/sigarh/creacion-roles/medicos/ordinario/[id]" data-perfil="Elaborador de roles (datos de prueba)"></div>
<figcaption>Figura 3. Editor de un rol de turno.</figcaption></figure>

<ol class="leyenda">
<li><strong>Encabezado.</strong> Servicio, modalidad, período y estado del rol.</li>
<li><strong>Progreso.</strong> Los cinco pasos y su porcentaje.</li>
<li><strong>Personal.</strong> Cada empleado con sus actividades y, dentro de ellas, sus turnos.</li>
<li><strong>Diagnóstico.</strong> Errores y advertencias que se actualizan con cada cambio.</li>
<li><strong>Enviar a revisión.</strong></li>
</ol>

Mientras el rol está en **Borrador** o **Rechazado**, se puede modificar. Si fue rechazado, un aviso muestra *Rol rechazado: corrígelo y vuelve a enviarlo* junto con el motivo.

## 3.1 Agregar personal

<ol class="pasos">
<li>Pulse <strong>Agregar personal</strong>. Se abre <em>Empleados del servicio seleccionado</em>.</li>
<li>Busque por nombre o DNI (<em>Buscar por nombre o DNI…</em>) y marque a los empleados. Los ya agregados no vuelven a aparecer.</li>
<li>Confirme. Mientras no haya nadie, el rol muestra <em>Sin personal todavía</em>.</li>
</ol>

Para quitar a alguien, use **Quitar del rol** (pide confirmación: *¿Quitar a este empleado del rol?*).

| Regla | Mensaje |
|---|---|
| El empleado debe corresponder a la **categoría de personal** del rol, según su tipo de trabajador y grupo ocupacional. | *No corresponden a la categoría … de este rol: … Revisa su tipo de trabajador o grupo ocupacional en Mantenimiento.* |
| Un empleado **no puede estar en dos roles ordinarios** del mismo servicio y período. | *… ya pertenece a otro rol ordinario de este servicio para MM/AAAA.* |

## 3.2 Agregar actividades

<ol class="pasos">
<li>En el empleado, pulse <strong>Actividades</strong> para abrir <em>Agregar actividades</em>.</li>
<li>Busque (<em>Buscar actividad…</em>) y marque las que correspondan. Las actividades que requieren consultorio llevan la etiqueta <strong>Consultorio</strong>.</li>
<li>Confirme. Use <strong>Quitar actividad</strong> para deshacer.</li>
</ol>

!!! note "Nota"
    Las actividades **asistenciales** son las que generan cupos de atención. Una actividad que requiere consultorio avisa: *Esta actividad requiere consultorio. El consultorio se asigna en la agenda de Consulta Externa.*

## 3.3 Agregar turnos

Cada actividad necesita al menos un turno. Pulse **Agregar turno** en la actividad:

| Campo | Descripción |
|---|---|
| **Turno / guardia** | Elija un horario (*Seleccione un horario*). La hora de inicio y de término se toman del horario seleccionado. |
| **Días de atención** | Marque los días **Dom, Lun, Mar, Mié, Jue, Vie, Sáb**. Los accesos **Lunes a viernes**, **Todos** y **Ninguno** ahorran clics. |

Para borrar un turno use **Quitar turno**.

## 3.4 Enviar a revisión

Cuando el diagnóstico no muestra errores, pulse **Enviar a revisión**. El sistema pregunta: *¿Enviar el rol a revisión? Ya no podrás editarlo salvo que sea rechazado.*

- Si hay errores: *Corrige los errores del diagnóstico antes de enviar.*
- Si el rol ya se envió: *El rol ya fue enviado.*
- Si todo está bien, el rol pasa a **Pendiente** y vuelve a la lista.
- El sistema vuelve a revisar todo al enviar: *No se puede enviar el rol: …* y los primeros problemas.
- Una vez enviado, el rol **no se puede editar** hasta que sea rechazado.
