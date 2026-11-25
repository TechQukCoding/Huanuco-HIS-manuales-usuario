# 3. La cirugía: del preoperatorio a la recuperación

Ruta: desde **Programación de Sala** o **Recuperación**, pulse **Abrir** en la cirugía. La pantalla *Cirugía* reúne todo el acto: *evaluaciones y consentimientos, lista de verificación OMS, tiempos y conteos, anestesia, informe operatorio y recuperación*.

<figure class="captura"><div class="marco"><img src="img/cq-cirugia.png" alt="Detalle de una cirugía" data-ruta="/app/centro-quirurgico/cirugia/[id]" data-perfil="Cirujano (datos de prueba)"></div>
<figcaption>Figura 2. Detalle de una cirugía.</figcaption></figure>

Tiene cinco secciones: **Preoperatorio**, **Intraoperatorio**, **Anestesia**, **Informe** y **Recuperación**. Si algo impide avanzar, un aviso lo lista: *Para continuar falta …*. El botón **Informe PDF** descarga el informe operatorio, y **Suspender cirugía** la detiene con un motivo (*Suspendida: …*).

!!! important "Importante"
    **El paciente no puede ingresar a sala sin cumplir cuatro requisitos**: evaluación **preoperatoria apta**, evaluación **preanestésica apta**, **consentimiento quirúrgico** y **consentimiento anestésico** vigentes, y un **anestesiólogo asignado**. Solo en una **emergencia** se puede exceptuar con **Registrar excepción de emergencia**, escribiendo la justificación; la excepción queda a la vista en la cirugía.

## 3.1 Preoperatorio

**Evaluaciones.** Registre la **evaluación preoperatoria** y la **preanestésica** con **Guardar evaluación**:

| Campo | Descripción |
|---|---|
| Evaluador | Obligatorio. Quién evalúa. |
| ASA | Clasificación de riesgo anestésico (I a VI, y las variantes de emergencia). Obligatorio en la preanestésica. |
| Mallampati | Obligatorio en la preanestésica: *La evaluación preanestésica requiere ASA y Mallampati*. |
| Riesgo quirúrgico | Obligatorio en la preoperatoria: *La evaluación preoperatoria requiere el riesgo quirúrgico*. |
| Horas de ayuno, Vía aérea, Exámenes revisados, Alergias, Plan | Opcionales. |
| Apto | Debe quedar marcado como apto para poder entrar a sala. |

**Consentimientos informados.** Con **Registrar consentimiento**, elija el **Tipo** (**Quirúrgico** o **Anestésico**) y complete **Firmante**, **DNI del firmante**, **Relación con el paciente** y **Riesgos explicados**. Solo puede haber **un consentimiento vigente por tipo**: *Ya hay un consentimiento vigente de ese tipo; revóquelo para registrar otro*. Use **Revocar** si el paciente lo retira (*El consentimiento ya fue revocado* si ya se hizo), solo antes de entrar a sala.

## 3.2 Intraoperatorio

### Lista de verificación de seguridad

Se completa en **tres fases**, en orden: **Entrada** (antes de la inducción), **Pausa** (antes de la incisión) y **Salida** (antes de salir de sala). En cada fase marque cada ítem como **Conforme** o **No conforme**.

| Regla | Mensaje |
|---|---|
| Debe responder todos los ítems. | *Responda todos los ítems de la fase* |
| Un ítem no cumplido requiere observación. | *Todo ítem no cumplido requiere observación* |
| La fase Entrada exige el ingreso a sala. | *Registre primero el ingreso a sala* |
| Cada fase se registra una sola vez. | *Esta fase de la lista de verificación ya fue registrada* |

### Tiempos del acto

Registre cada momento, **en este orden**: **Ingreso a sala**, **Inicio de anestesia**, **Incisión**, **Cierre**, **Fin de anestesia** y **Salida de sala**. Si omite uno, el sistema avisa *Registre antes: …*. Cada momento se registra una vez (*Ese momento ya fue registrado*), con una hora que no sea futura ni anterior al momento previo.

### Conteo de gasas, compresas, agujas e instrumental

Se hacen **dos conteos**: el **inicial**, antes de la incisión, y el **final**, entre la incisión y el cierre. Si el resultado es **No conforme**, la observación es obligatoria (*Un conteo no conforme requiere observación*).

### Insumos y material esterilizado

Con **Registrar insumo**, escriba el **Insumo y lote**, la **Cantidad** y, si es un implante, el **Número de serie** (*Un implante requiere número de serie*). Si el material viene de la Central de Esterilización, su lote debe estar liberado: *El lote no está liberado para uso* (capítulo 5).

## 3.3 Anestesia

En **Acto anestésico** complete el **Tipo de anestesia** (**General**, **Regional**, **Local**, **Sedación** o **Combinada**), el **ASA**, el **Anestesiólogo**, la **Técnica**, los **Agentes y dosis**, los **Líquidos y balance** y las observaciones, y pulse **Guardar acto anestésico**. Antes de registrar insumos o controles debe existir el tipo de anestesia (*Registre primero el tipo de anestesia*).

En **Monitorización intraoperatoria**, pulse **Agregar control** para anotar **Hora**, **PA**, **FC**, **SpO2**, **EtCO2** y un **Evento**.

## 3.4 Informe operatorio

| Campo | Descripción |
|---|---|
| Diagnóstico postoperatorio (CIE-10) | Obligatorio para firmar. |
| Procedimiento realizado | Obligatorio para firmar. |
| Técnica | Obligatoria para firmar. |
| Hallazgos | Obligatorios para firmar. |
| Complicaciones, Drenajes, Sangrado estimado (ml) | Opcionales. |
| Muestra | Si se envía una pieza a patología, descríbala: *Describa la muestra enviada a anatomía patológica*. |

Use **Guardar borrador** para conservar lo escrito y **Firmar informe** para cerrarlo con su **PIN**.

!!! important "Importante"
    **Solo el cirujano principal firma el informe**, y solo cuando ya registró la **salida de sala**. Si falta algo: *Complete antes de firmar: …*. Si no es el cirujano: *Solo el cirujano principal firma el informe operatorio*. Un informe firmado no se modifica (*El informe ya está firmado*).

## 3.5 Recuperación

<ol class="pasos">
<li>Pulse <strong>Registrar ingreso a recuperación</strong> cuando el paciente llegue a URPA.</li>
<li>Con <strong>Agregar control</strong>, anote la <strong>Hora</strong>, el <strong>Aldrete (0 a 10)</strong> —obligatorio—, la <strong>PA</strong>, la <strong>FC</strong>, la <strong>SpO2</strong>, el <strong>Dolor EVA</strong> y una observación, indicando al <strong>Responsable de recuperación</strong>.</li>
<li>Cuando el paciente esté listo, pulse <strong>Dar alta de recuperación</strong> y elija el <strong>Destino</strong> (<em>Hospitalización</em>, <em>UCI</em>, <em>Alta</em>, <em>Referencia</em> o <em>Fallecido</em>), con el detalle del servicio o la cama.</li>
</ol>
