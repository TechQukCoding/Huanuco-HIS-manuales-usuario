# 2. Empleados

El registro de **Empleados** es la base de SIGARH: de él salen los médicos que firman atenciones, el personal de los roles de turno, la asistencia y todos los movimientos. **Registre primero a las personas y después cree sus cuentas** (manual SIG-04).

Ruta: **SIGARH › Recursos Humanos › Empleados**.

## 2.1 Listado

<figure class="captura"><div class="marco"><img src="img/rrhh-empleados-listado.png" alt="Listado de empleados" data-ruta="/sigarh/rrhh/empleados" data-perfil="Personal de RR. HH. (datos de prueba)"></div>
<figcaption>Figura 1. Listado de empleados.</figcaption></figure>

<ol class="leyenda">
<li><strong>Nuevo empleado.</strong></li>
<li><strong>Indicadores.</strong> Total, Activos, Inactivos y Antigüedad media.</li>
<li><strong>Búsqueda y pestañas.</strong> Busque por nombre, DNI o cargo; filtre por <em>Todos</em>, <em>Activos</em> o <em>Inactivos</em>.</li>
<li><strong>Tabla.</strong> Empleado (con su correo), DNI, Cargo, Modalidad, Antigüedad y Estado.</li>
</ol>

El menú de acciones de cada fila ofrece **Ver y editar** y **Eliminar**.

## 2.2 Registrar un empleado

El alta es un asistente de **5 pasos**. Para avanzar se usa **Siguiente**, que valida el paso; solo puede volver a un paso ya visitado con **Anterior** o desde la barra de pasos.

<div class="flujo">
<span class="paso ok">1. Datos personales</span><span class="flecha">›</span>
<span class="paso ok">2. Datos laborales</span><span class="flecha">›</span>
<span class="paso">3. Especialidades</span><span class="flecha">›</span>
<span class="paso">4. Datos bancarios</span><span class="flecha">›</span>
<span class="paso">5. Ubicación</span>
</div>

Si falta algún dato obligatorio, el sistema indica *Completa los campos requeridos de este paso.*

### Paso 1: Datos personales

<figure class="captura"><div class="marco"><img src="img/rrhh-empleado-paso1.png" alt="Alta de empleado, paso Datos personales" data-ruta="/sigarh/rrhh/empleados/create" data-perfil="Personal de RR. HH. (datos de prueba)"></div>
<figcaption>Figura 2. Alta de empleado: datos personales.</figcaption></figure>

<ol class="pasos">
<li>Escriba el <strong>DNI</strong> (8 dígitos). El sistema verifica por sí solo si ya existe: mientras tanto indica <em>Verificando disponibilidad…</em> y, si está libre, <em>DNI disponible</em>.</li>
<li>Pulse <strong>Consultar DNI</strong> para traer los nombres desde RENIEC. Revise los datos: <em>Datos traídos del servicio de identidad. Verifícalos.</em></li>
<li>Complete los demás datos personales (tabla siguiente).</li>
<li>Pulse <strong>Siguiente</strong>.</li>
</ol>

!!! important "Importante"
    **Un DNI ya registrado no permite avanzar**: corrija el número o abra el empleado existente desde el listado.

!!! tip "Consejo"
    Si el servicio de identidad no encuentra el DNI (*El DNI no figura en el servicio…*) o no responde (*El servicio de identidad no respondió…*), active el interruptor **Registro manual** e ingrese los datos a mano. Con ese interruptor activo, la consulta a RENIEC queda deshabilitada.

| Campo | Obligatorio | Descripción |
|---|:-:|---|
| DNI | <span class="si">Sí</span> | 8 dígitos. *El DNI es requerido*. |
| Nombres | <span class="si">Sí</span> | Nombres completos. |
| Apellido paterno / Apellido materno | <span class="si">Sí</span> | Se validan como nombres. |
| Fecha de nacimiento | <span class="si">Sí</span> | *La fecha de nacimiento es requerida*. |
| Sexo | <span class="si">Sí</span> | Femenino o Masculino. |
| Estado civil | <span class="si">Sí</span> | Soltero(a), Casado(a), Conviviente, Divorciado(a) o Viudo(a). |
| Celular | <span class="si">Sí</span> | **9 dígitos**. Si no: *El celular debe tener 9 dígitos*. |
| Correo electrónico | <span class="si">Sí</span> | Con formato de correo: *El correo no tiene un formato válido*. |
| Grupo sanguíneo | <span class="no">No</span> | Por defecto *Sin registrar*. |
| Teléfono fijo | <span class="no">No</span> | Opcional. |

### Paso 2: Datos laborales

| Campo | Obligatorio | Descripción |
|---|:-:|---|
| Tipo de trabajador | <span class="no">No</span> | Catálogo de Mantenimiento (manual SIG-04). |
| Nivel remunerativo | <span class="no">No</span> | Catálogo de Mantenimiento. |
| Modalidad | <span class="no">No</span> | CAS, Contrato, Nombrado, SNP o Tercero. |
| Régimen laboral y Condición laboral | Según el régimen | Elija el régimen y luego su condición; si falta: *Selecciona la condición del régimen laboral elegido.* |
| Profesión | <span class="no">No</span> | Catálogo de profesiones. **Determina el grupo ocupacional**. |
| Grupo ocupacional | <span class="si">Sí</span> | Se asigna según la profesión elegida. *El grupo ocupacional es requerido*. |
| Colegio profesional / Número de colegiatura | <span class="no">No</span> | Datos del colegio profesional del empleado. |
| N.° CMP | <span class="no">No</span> | **Solo médicos.** |
| Código MINSA | <span class="no">No</span> | Código del empleado en MINSA. |
| Departamento | <span class="no">No</span> | Por defecto *Sin departamento*. |
| Servicio / Área | <span class="si">Sí</span> | *El servicio es requerido*. |
| Dependencia | <span class="no">No</span> | Se usa para calcular **la tolerancia de tardanza** que le aplica (capítulo 3). |
| Cargo laboral | <span class="si">Sí</span> | *El cargo laboral es requerido*. |
| Fecha de ingreso | <span class="si">Sí</span> | Debe ser posterior al nacimiento. El sistema calcula la **antigüedad** automáticamente. |
| Fecha y resolución de nombramiento | <span class="no">No</span> | Para personal nombrado. |
| Fecha y resolución de cese | <span class="no">No</span> | Ver 2.4. |
| Horas ordinarias mensuales y Sustento de la jornada | Personal médico | Jornada del médico y su sustento. |

Además hay un bloque de **Legajo** con datos de respaldo: **Número de legajo**, **Título o formación acreditada**, **Institución de formación**, **Fecha del título**, **Documento del vínculo laboral**, **Contacto de emergencia** y **Teléfono de emergencia**.

!!! note "Nota"
    El **servicio** del empleado se usa, por ejemplo, para validar los cambios de turno: el aceptante debe pertenecer al servicio de la agenda que cubriría (capítulo 8).

### Paso 3: Especialidades (solo médicos)

Este paso solo se habilita si en el paso anterior se eligió la profesión **Médico Cirujano**; en otro caso aparece *Las especialidades solo aplican al personal médico.* Pulse para agregar cada **Especialidad** con su **N.° RNE** (registro nacional de especialista). Sin ninguna, se muestra *Sin especialidades registradas*.

### Paso 4: Datos bancarios

| Campo | Descripción |
|---|---|
| Banco | Entidad donde se abona la remuneración. Por defecto *Sin banco*. |
| Tipo de cuenta | **Ahorros** o **Corriente**. |
| Número de cuenta | Entre **10 y 20 dígitos**. |
| Número CCI | Código de cuenta interbancario. |
| RUC | RUC del trabajador, si corresponde. |

### Paso 5: Ubicación

**Departamento**, **Provincia**, **Distrito** y **Dirección**. Si el catálogo de ubigeo aún no tiene datos, el sistema avisa: *Puedes registrar la dirección; departamento, provincia y distrito quedarán pendientes.*

Al terminar, pulse **Crear empleado**. Con el interruptor **Empleado activo** decide si aparece desde ese momento en los selectores de SIGARH.

## 2.3 Editar un empleado

Abra el empleado con **Ver y editar** (*Actualiza la ficha del colaborador*), cambie los datos y pulse **Guardar cambios**. La ficha tiene los mismos datos del alta.

## 2.4 Cese y estado Activo

!!! important "Importante"
    **Para dar de baja a un empleado, registre la resolución y la fecha de cese.** El interruptor **Activo** solo controla si la persona aparece en los selectores: no reemplaza el cese.

El sistema usa las fechas de **ingreso** y de **cese** para impedir programar a una persona fuera de su vínculo: *La fecha programada es anterior al ingreso del trabajador* o *La fecha programada es posterior al cese del trabajador*. Un trabajador inactivo no se puede programar (*El trabajador esta inactivo o no existe*).

## 2.5 Reglas de validación y mensajes

| Situación | Mensaje del sistema | Qué hacer |
|---|---|---|
| El correo ya pertenece a otro empleado | *Ya existe un empleado con el correo …* | Use otro correo o abra al empleado existente. |
| El servicio no es del departamento elegido | *El servicio no pertenece al departamento seleccionado.* | Elija un servicio del departamento o cambie el departamento. |
| La fecha de ingreso es anterior al nacimiento | *La fecha de ingreso debe ser posterior al nacimiento.* | Corrija la fecha. |
| El grupo ocupacional no corresponde a la profesión | *El grupo ocupacional no corresponde a la profesión seleccionada.* | Elija la profesión y deje que el sistema asigne el grupo. |
| Habilitación verificada sin colegio ni colegiatura | *Para registrar habilitación verificada se requiere colegio y número de colegiatura.* | Complete **Colegio profesional** y **Número de colegiatura**. |
| El régimen o la condición no están vigentes | *Seleccione un régimen y condición laboral vigentes del catálogo.* | Elija valores activos. |
| El tipo de trabajador no corresponde al vínculo laboral | *El tipo de trabajador no corresponde al vínculo laboral registrado.* | Elija un tipo coherente con el régimen. |
| El nivel remunerativo no corresponde a la profesión | *El nivel remunerativo no corresponde a la profesión del trabajador.* | Elija un nivel que corresponda. |
| Especialidades sin la profesión de médico | *Selecciona la profesión Médico Cirujano para asignar especialidades.* | Cambie la profesión a **Médico Cirujano**. |
| Cambiar la profesión con especialidades cargadas | *Retira las especialidades médicas antes de cambiar la profesión.* | Quite primero las especialidades del empleado. |
| Especialidad repetida | *La especialidad ya está asignada al empleado.* | No repita la misma especialidad. |
