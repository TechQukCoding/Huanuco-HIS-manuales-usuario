# 3. Infraestructura hospitalaria: pisos, salas y camas

La estructura física se arma de arriba abajo: **pisos**, **salas** (con su servicio) y **camas**.

<div class="flujo">
<span class="paso ok">Piso</span><span class="flecha">›</span>
<span class="paso ok">Servicio (SIG-04)</span><span class="flecha">›</span>
<span class="paso">Sala</span><span class="flecha">›</span>
<span class="paso">Cama</span>
</div>

## 3.1 Pisos

Ruta: **Infraestructura Hospitalaria › Pisos** (*Niveles físicos del hospital*). La lista muestra Nombre, Orden, Servicios, Salas y Estado.

| Campo | Obligatorio | Descripción |
|---|:-:|---|
| Nombre del piso | <span class="si">Sí</span> | Ej.: *Segundo piso*, *Sótano*. Máximo 100 caracteres. |
| Orden de visualización | <span class="no">No</span> | Posición en los listados. **No es el número físico del piso.** |
| Descripción | <span class="no">No</span> | Ubicación o características. |

Luego se le asignan **servicios** desde Mantenimiento (SIG-04); las salas se vinculan al piso por esos servicios.

!!! important "Importante"
    Un piso con servicios, salas o consultorios asociados no se puede eliminar: *No se puede eliminar: el piso tiene N servicio(s) y N sala(s) asociados.* Reasigne esos registros primero, o desactive el piso.

## 3.2 Salas

Ruta: **Infraestructura Hospitalaria › Salas** (*Ambientes por servicio y su capacidad de camas*).

<figure class="captura"><div class="marco"><img src="img/infra-salas.png" alt="Lista de salas" data-ruta="/sigarh/infraestructura-hosp/salas" data-perfil="Administrador SIGARH (datos de prueba)"></div>
<figcaption>Figura 2. Salas del hospital.</figcaption></figure>

- **Indicadores:** Total salas, Capacidad total, Camas disponibles y Camas ocupadas.
- **Filtros:** buscador por nombre o código y selector **Todos los pisos**.
- **Tabla:** Nombre, Código, Piso, Servicio, Capacidad y Camas.

| Campo | Obligatorio | Descripción |
|---|:-:|---|
| Piso | <span class="no">No</span> | Auxiliar: filtra los servicios por piso. |
| Servicio | <span class="si">Sí</span> | Vincula la sala con el servicio responsable. |
| Nombre de la sala | <span class="si">Sí</span> | Máximo 100 caracteres. Ej.: *Habitación 301*. |
| Código | <span class="no">No</span> | Ej.: *H301*. También sirve de prefijo al generar camas. |
| Capacidad | <span class="si">Sí</span> | Número de camas. El formulario indica cuántas hay registradas. |
| Tipo de ambiente | <span class="si">Sí</span> | **General (hospitalización, observación)**, **Quirófano**, **Recuperación postanestésica**, **Cuidados intensivos (UCI)**, **Cuidados intermedios**, **UCI neonatal**, **UCI pediátrica** u **Observación de emergencia**. Quirófano, UCI e Intermedios son de uso exclusivo de su unidad; Hospitalización usa las camas de salas generales. |
| Sala activa | — | Las inactivas no se ofrecen para asignar camas. |

### Generar camas de una sala

Para no crear las camas una por una, use **Generar camas** en el menú de la sala. El diálogo indica cuántas faltan (por ejemplo, *faltan 3 de 6*).

<ol class="pasos">
<li>Elija <strong>Generar camas</strong> en la sala.</li>
<li>Escriba el <strong>Prefijo del código</strong>. Por ejemplo, <code>H</code> genera H01, H02…</li>
<li>Elija el <strong>Tipo de cama</strong> (catálogo <em>Tipos de cama</em>).</li>
<li>Confirme. El sistema crea las camas que faltan hasta completar la capacidad.</li>
</ol>

!!! important "Importante"
    No se puede eliminar una sala con camas ocupadas: *No se puede eliminar: la sala tiene N cama(s) ocupada(s).*

## 3.3 Camas

Ruta: **Infraestructura Hospitalaria › Camas** (*Camas individuales, ubicación, tipo y estado*).

- **Indicadores y pestañas:** Todas, **Disponibles**, **Ocupadas**, **Mantenimiento** y **Reservadas**.
- **Tabla:** Código, Nombre, Sala, Tipo y Estado. El menú de cada cama ofrece **Cambiar estado**, **Ver y editar** y **Eliminar**.

!!! important "Importante"
    **Una cama con un paciente internado no cambia de estado aquí**: el alta se registra desde **Hospitalización** (HIS). Tampoco se elimina una cama ocupada. La sala y la cama deben coincidir en piso y servicio.

| Campo | Obligatorio | Descripción |
|---|:-:|---|
| Piso | <span class="no">No</span> | Auxiliar: filtra las salas. |
| Sala | <span class="no">No</span> | Al elegirla se completan servicio y piso (texto que se puede ajustar). *Sin sala (solo texto)* si no corresponde. |
| Código | <span class="si">Sí</span> | **Único**, en mayúsculas, máximo 20 caracteres. Ej.: *UCI-01*. Si ya existe: *Ya existe una cama con el código …* |
| Nombre / descripción | <span class="si">Sí</span> | Máximo 100 caracteres. Ej.: *Cama 1 — Sala A*. |
| Tipo de cama | <span class="si">Sí</span> | Del catálogo *Tipos de cama*. |
| Estado | <span class="si">Sí</span> | **Disponible**, **Ocupada**, **Mantenimiento**, **Reservada**, **Limpieza** o **Bloqueada**. Es independiente del interruptor *Cama activa*: una cama activa puede estar ocupada. |
