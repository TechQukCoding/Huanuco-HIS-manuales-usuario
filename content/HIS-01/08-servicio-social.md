# 8. Servicio Social

Ruta: **Servicio Social › Servicio Social** (*Evaluaciones sociales, gestiones y seguimiento de casos*). Cada paciente evaluado tiene un **caso** con sus **gestiones**, que permanece **abierto** hasta que se cierra.

<div class="flujo">
<span class="paso ko">Evaluación (caso abierto)</span><span class="flecha">›</span>
<span class="paso">Gestiones</span><span class="flecha">›</span>
<span class="paso ok">Caso cerrado</span>
</div>

## 8.1 Registrar una evaluación social

<figure class="captura"><div class="marco"><img src="img/ss-evaluacion.png" alt="Nueva evaluación social" data-ruta="/app/servicio-social/servicio-social" data-perfil="Trabajador social (datos de prueba)"></div>
<figcaption>Figura 9. Nueva evaluación social.</figcaption></figure>

Pulse **Nueva evaluación**.

| Campo | Obligatorio | Descripción |
|---|:-:|---|
| ID del paciente | <span class="si">Sí</span> | Identificador del paciente (ver el aviso de abajo). |
| ID del trabajador social | <span class="si">Sí</span> | Identificador del empleado. **Debe tener la profesión Trabajador Social (TSO)** en SIGARH. |
| Origen (opcional) | <span class="no">No</span> | **Directo**, **Consulta Externa**, **Emergencia** u **Hospitalización**. Si elige uno, aparece **ID del origen**. |
| Tipo de vivienda | <span class="no">No</span> | Propia, Alquilada, Alojada, Asentamiento humano o Sin vivienda. |
| Clasificación socioeconómica (referencial) | <span class="no">No</span> | No pobre, Pobre o Pobre extremo. |
| Red de apoyo familiar | <span class="no">No</span> | Descripción libre. |
| Factores de riesgo social | <span class="no">No</span> | Marque los que apliquen: **Violencia familiar**, **Abandono**, **Situación de calle**, **Adulto mayor solo**, **Discapacidad sin soporte** y **Menor en riesgo**. |
| Requiere derivación externa | — | Si se marca, elija la **Entidad de derivación**: **MIMP**, **CEM**, **INABIF**, **DEMUNA** u **Otro**. |
| Recomendaciones | <span class="no">No</span> | Indicaciones del trabajador social. |

!!! important "Importante"
    En esta versión, la pantalla pide los **identificadores internos (UUID)** del paciente y del trabajador social, no un buscador. Se obtienen de la dirección de su ficha: en la ficha del paciente (`/app/admision/pacientes/<id>`) y en la del empleado en SIGARH (`/sigarh/rrhh/empleados/<id>`), copiando el código largo que aparece al final de la dirección.

Si el empleado no es trabajador social: *El profesional debe tener profesión Trabajador Social (TSO) registrada*. Si el paciente no existe: *Paciente no encontrado*.

## 8.2 Registrar gestiones y cerrar el caso

Los casos se listan con el filtro **Todos / Abierto / Cerrado**, con su estado, el trabajador social, la fecha, la clasificación y las gestiones ya registradas (Fecha, Tipo, Descripción y **Por** quién).

<ol class="pasos">
<li>En un caso <strong>abierto</strong>, elija el <strong>tipo de gestión</strong>: <strong>Visita domiciliaria</strong>, <strong>Llamada telefónica</strong>, <strong>Coordinación interinstitucional</strong>, <strong>Entrevista</strong>, <strong>Gestión de apoyo social</strong> u <strong>Otro</strong>.</li>
<li>Escriba la <strong>descripción de la gestión</strong> (sin ella, el botón queda deshabilitado) y pulse <strong>Registrar gestión</strong>.</li>
<li>Cuando el caso termine, pulse <strong>Cerrar caso</strong>. Aparece <em>Caso cerrado.</em></li>
</ol>

!!! note "Nota"
    Un caso cerrado no admite nuevas gestiones (*No se pueden registrar gestiones en un caso cerrado*) ni se puede cerrar otra vez (*Este caso ya está cerrado*). Si hace falta continuar, registre una nueva evaluación.
