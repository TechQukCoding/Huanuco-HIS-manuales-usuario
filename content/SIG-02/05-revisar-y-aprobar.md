# 5. Revisar y aprobar roles

Ruta: **SIGARH › Roles Pendientes › Bandeja de Roles** (*Bandeja de roles enviados a revisión*).

## 5.1 La bandeja

<figure class="captura"><div class="marco"><img src="img/pendientes-bandeja.png" alt="Bandeja de roles pendientes" data-ruta="/sigarh/roles-pendientes" data-perfil="Revisor con permiso Aprobar roles de turno (datos de prueba)"></div>
<figcaption>Figura 4. Bandeja de roles pendientes.</figcaption></figure>

- **Indicadores:** Roles por revisar, Servicios, Personal involucrado y Programación incompleta.
- **Tabla:** Servicio, Período, Modalidad, Personal y **Enviado por**.
- **Acciones:** **Revisar** abre el rol; el botón **Solicitudes de modificación** lleva a las incorporaciones de personal (capítulo 6).

## 5.2 Revisar un rol

La pantalla **Revisar rol** muestra la programación completa y el resultado del diagnóstico:

- **El rol está listo: todas las actividades asistenciales generarán cupos.** Puede aprobarlo.
- **No se puede aprobar: N problemas que impiden generar cupos.** Hay errores; devuélvalo.
- **N advertencias.** No bloquean la aprobación.

### Aprobar

Pulse **Aprobar**. Al aprobarse:

1. El rol pasa a **Aprobado** y se registra quién lo revisó y cuándo.
2. El sistema **sincroniza la programación con la agenda de Consulta Externa**: se abren los cupos del mes.
3. Se envía una **notificación** (*Rol de turno aprobado: mes/año*).
4. Si al sincronizar hay **citas ya tomadas que quedan sin médico de respaldo**, se envía además una alerta: *N cita(s) requieren reprogramación*.

### Rechazar

<ol class="pasos">
<li>Pulse <strong>Rechazar</strong>. Se abre <em>Rechazar rol</em>: <em>El rol vuelve a Creación de Roles para que lo corrijan.</em></li>
<li>Escriba el <strong>Motivo del rechazo</strong> (<em>Explica qué debe corregirse…</em>). Mínimo <strong>5 caracteres</strong>.</li>
<li>Pulse <strong>Confirmar rechazo</strong>. El rol pasa a <strong>Rechazado</strong> y se notifica el motivo.</li>
</ol>

## 5.3 Quién puede aprobar

| Regla | Mensaje |
|---|---|
| Su rol debe incluir el permiso **Aprobar roles de turno** (manual SIG-04, sección 3.4). | *No tiene permiso para aprobar roles de turno de este servicio.* |
| Sin **alcance global**, solo puede aprobar roles de los servicios donde usted es **jefe del servicio** (SIG-04, sección 3.5). | *No tiene permiso para revisar roles de turno de este servicio.* |
| **Quien elaboró el rol no puede aprobarlo.** | *Quien elaboró el rol no puede aprobarlo; debe revisarlo otra persona.* |
| Solo se decide un rol **pendiente**. | *Solo se pueden aprobar / rechazar roles en estado pendiente.* |
| El diagnóstico se vuelve a ejecutar al aprobar. | *No se puede aprobar el rol: …* |

!!! important "Importante"
    Aprobar es **definitivo para la agenda**: abre cupos y puede dejar citas en riesgo. Revise las advertencias antes de aprobar y avise al servicio si hay citas por reprogramar.
