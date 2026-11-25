# 9. Papeletas

Una **papeleta** autoriza la **salida de un trabajador durante su jornada** y registra su retorno. Se maneja con **Tramitar Papeleta** y **Estado de Papeletas**.

## 9.1 Tramitar una papeleta

Ruta: **Movimientos › Papeletas › Tramitar Papeleta** (*Solicitud de salida del trabajador durante la jornada*).

<figure class="captura"><div class="marco"><img src="img/mov-papeleta-tramitar.png" alt="Tramitar papeleta" data-ruta="/sigarh/movimientos/papeletas/tramitar" data-perfil="Personal de RR. HH. (datos de prueba)"></div>
<figcaption>Figura 5. Tramitar papeleta.</figcaption></figure>

<ol class="pasos">
<li>Busque al trabajador por su <strong>DNI del trabajador</strong>.</li>
<li>Elija el <strong>Motivo de la salida</strong>: <strong>Asuntos particulares</strong>, <strong>Comisión</strong>, <strong>Salud</strong>, <strong>Trámite personal</strong> u <strong>Otro</strong>.</li>
<li>Escriba el <strong>N.° de documento</strong> (por ejemplo <code>PAP-0123-2026</code>).</li>
<li>Si el motivo es <strong>Salud</strong>, adjunte el enlace del <strong>Documento sustentatorio</strong>: es obligatorio.</li>
<li>En <strong>Detalle</strong> indique a dónde va y por cuánto tiempo aproximadamente.</li>
<li>Pulse <strong>Tramitar papeleta</strong>. La <strong>fecha de trámite</strong> es la de hoy.</li>
</ol>

| Regla | Mensaje |
|---|---|
| El empleado no puede tener otra papeleta pendiente o aprobada el mismo día. | *El empleado ya tiene una papeleta pendiente o aprobada para ese día* |
| El motivo Salud exige documento. | *Para el motivo 'Salud' es obligatorio adjuntar el documento sustentatorio* |
| Solo se edita una papeleta pendiente. | *La papeleta ya fue …; no se puede editar* |

## 9.2 Autorizar, rechazar y registrar el retorno

Ruta: **Movimientos › Papeletas › Estado de Papeletas** (*Autoriza la salida y registra el retorno del personal*).

- **Indicadores:** Papeletas, Por autorizar, Aprobadas, **Fuera (sin retorno)** y Rechazadas.
- **Columnas:** Trabajador, Fecha, Motivo, **Salida › retorno** y Estado. Las personas que salieron y aún no volvieron muestran la etiqueta **Fuera**.

<ol class="pasos">
<li>Para una papeleta <strong>Pendiente</strong>, pulse <strong>Autorizar</strong>. El sistema registra la <strong>hora de salida</strong> con la hora actual de Lima.</li>
<li>Si no procede, pulse <strong>Rechazar</strong> y escriba el <strong>Motivo del rechazo</strong>.</li>
<li>Cuando el trabajador regrese, pulse <strong>Registrar retorno</strong>. El sistema registra la <strong>hora de retorno</strong> con la hora actual de Lima.</li>
</ol>

!!! important "Importante"
    El retorno solo se puede registrar en una papeleta **aprobada** y **una sola vez**: *Solo se puede registrar el retorno de una papeleta aprobada* / *El retorno ya fue registrado*. Las horas las pone el sistema; no se escriben a mano.

El resultado (aprobada o rechazada) se notifica en las **Notificaciones** de SIGARH. Con **Ver documento** abre el enlace sustentatorio.
