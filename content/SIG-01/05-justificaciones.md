# 5. Justificaciones e inasistencias

Esta pantalla registra y consulta las **ausencias y permisos** del personal con su sustento. Una justificación aprobada marca la asistencia del período como **Justificado**.

Ruta: **SIGARH › Recursos Humanos › Justificaciones e Inasistencias**.

## 5.1 Listado

<figure class="captura"><div class="marco"><img src="img/rrhh-justificaciones.png" alt="Listado de justificaciones e inasistencias" data-ruta="/sigarh/rrhh/justificaciones" data-perfil="Personal de RR. HH. (datos de prueba)"></div>
<figcaption>Figura 1. Justificaciones e inasistencias.</figcaption></figure>

<ol class="leyenda">
<li><strong>Nueva justificación.</strong></li>
<li><strong>Indicadores.</strong> Justificaciones, Pendientes, Aprobadas, Rechazadas y Días justificados. Los totales de días y de estados corresponden a la página que está viendo.</li>
<li><strong>Filtros.</strong> <em>Todos los empleados</em>, <em>Todos los motivos</em> y el rango <em>Desde</em> / <em>Hasta</em>. Use <strong>Limpiar filtros</strong> para quitarlos.</li>
<li><strong>Tabla.</strong> Trabajador (con DNI y cargo), Motivo, Período, Días, Estado y Documento.</li>
</ol>

## 5.2 Registrar una justificación

<ol class="pasos">
<li>Pulse <strong>Nueva justificación</strong>.</li>
<li>Busque y elija al <strong>Empleado</strong> escribiendo su nombre.</li>
<li>Elija el <strong>Motivo</strong>, indique el <strong>N.° de documento</strong> y la <strong>Fecha de trámite</strong>.</li>
<li>Indique el período con <strong>Desde</strong> y <strong>Hasta</strong>. El sistema muestra cuántos días se justifican (cuenta el día de inicio y el de fin).</li>
<li>Elija el <strong>Estado inicial</strong> y escriba el sustento en <strong>Descripción / sustento</strong>.</li>
<li>Pulse <strong>Crear justificación</strong>.</li>
</ol>

| Campo | Obligatorio | Descripción |
|---|:-:|---|
| Empleado | <span class="si">Sí</span> | Se busca por nombre. Si falta: *El empleado es requerido*. |
| Motivo | <span class="no">No</span> | Recomendado: alimenta los reportes de ausentismo. Por defecto *Sin motivo específico*. |
| N.° de documento | <span class="no">No</span> | Hasta 50 caracteres. Ej.: MEMO-0123-2026. |
| Fecha de trámite | <span class="no">No</span> | Fecha en que se tramitó el documento. |
| Desde / Hasta | <span class="si">Sí</span> | *La fecha de inicio es requerida* y *La fecha de fin es requerida*. La fecha final no puede ser anterior a la inicial: *No puede ser anterior a la de inicio*. |
| Estado inicial | <span class="no">No</span> | **Pendiente** (queda para revisión), **Aprobado** (marca la asistencia como Justificado) o **Rechazado** (se conserva en el historial). |
| Descripción / sustento | <span class="no">No</span> | Detalle del permiso o la ausencia. |

## 5.3 Revisar y cambiar el estado

Haga clic en la justificación para abrirla. La pantalla indica *Revisa el sustento y define el estado de la solicitud*. Cambie el estado y pulse **Guardar cambios**.

!!! important "Importante"
    Al aprobar una justificación, la asistencia de ese período queda marcada como **Justificado**. Las justificaciones rechazadas no se borran: permanecen en el historial del empleado. Solo se pueden **eliminar** las justificaciones **pendientes**; una ya decidida no se elimina (*La solicitud ya fue …; no se puede eliminar*), porque dejaría la asistencia justificada sin respaldo.

!!! note "Nota"
    Esta pantalla sirve para registrar y corregir justificaciones por parte de RR. HH. Las solicitudes que llegan desde jefaturas se revisan en la bandeja **Justificación y vacaciones** (capítulo 6).
