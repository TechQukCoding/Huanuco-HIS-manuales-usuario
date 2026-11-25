# 8. Telesalud

**Telesalud** gestiona las **teleconsultas**: consultas a distancia con médicos que tienen programaciones **virtuales**. Tiene cinco opciones.

Una cita es **virtual** cuando su programación médica tiene la modalidad **Virtual** (manual HIS-01, capítulo 4).

## 8.1 Resumen de teleconsultas

*Citas virtuales, teleconsultas firmadas y no asistencia en el rango.* Elija **Desde** y **Hasta** (obligatorios) y pulse **Buscar**.

- **Indicadores:** **Citas virtuales programadas**, **Teleconsultas firmadas** y **Tasa de no asistencia** (con la cantidad de pacientes que no asistieron). La tasa se resalta cuando **supera el 20 %**.
- **Tabla por médico:** Médico, Especialidad, Citas y Teleconsultas firmadas.

## 8.2 Guía rápida MINSA

Pantalla de lectura con el **marco legal, las modalidades y la lista de verificación** de telesalud.

## 8.3 Monitor y médicos

- **Monitor** (*Teleconsultas programadas para hoy*): Fecha, Hora, Paciente, DNI, Médico y Estado de cada cita virtual del día.
- **Médicos** (*Médicos con programaciones virtuales*): Médico, DNI, CMP, Especialidades (con su RNE) y Contacto.

## 8.4 Formulario de solicitud

*Solicitudes de teleconsulta: registro, programación y rechazo.* Una solicitud es un pedido del paciente para ser atendido a distancia.

<ol class="pasos">
<li>Pulse <strong>Nueva solicitud</strong>.</li>
<li>Escriba el <strong>DNI o ID del paciente</strong> (obligatorio).</li>
<li>Elija el <strong>Medio preferido</strong>: <strong>Llamada</strong>, <strong>WhatsApp</strong> o <strong>Videollamada</strong>.</li>
<li>Escriba el <strong>Motivo</strong> (obligatorio) y, si es distinto del registrado, el <strong>Contacto</strong>.</li>
<li>Pulse <strong>Registrar solicitud</strong>. Queda <strong>Pendiente</strong>.</li>
</ol>

Las solicitudes se filtran por estado (**Todas**, **Pendiente**, **Programada**, **Rechazada**). Una solicitud **pendiente** se resuelve así:

- **Programar:** la enlaza con una **cita virtual** del mismo paciente. El botón se habilita cuando el paciente tiene una cita virtual por enlazar.
- **Rechazar:** la cierra sin programar.

| Regla | Mensaje |
|---|---|
| La cita debe ser del mismo paciente. | *La cita pertenece a otro paciente* |
| La cita debe tener modalidad virtual. | *La cita debe pertenecer a una programación con modalidad VIRTUAL* |
| Una cita se enlaza a una sola solicitud. | *Esa cita ya está enlazada a otra solicitud* |
