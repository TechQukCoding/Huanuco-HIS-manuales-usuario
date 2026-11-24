# 3. Roles del sistema

Un **rol del sistema** define el *techo* de acceso de un grupo de cuentas: en qué panel trabajan, qué módulos y submódulos pueden llegar a usar y qué acciones especiales pueden realizar. Los perfiles y los usuarios se construyen sobre él.

Ruta: **Mantenimiento › Roles del sistema**.

## 3.1 Listado

La lista muestra **Código**, **Nombre**, **Panel** (*Hospitalario* o *SIGARH*), **Descripción** y **Estado** (*Activo* / *Inactivo*). Se busca por nombre o código y funciona como se explica en el capítulo 2. En la parte superior un recuadro recuerda la cadena *Roles › Perfiles › Usuarios*.

## 3.2 Crear un rol

<figure class="captura"><div class="marco"><img src="img/mant-rol-crear.png" alt="Formulario Crear rol del sistema" data-ruta="/sigarh/mantenimiento/roles-sistema/create" data-perfil="Administrador SIGARH con Administrar Seguridad (datos de prueba)"></div>
<figcaption>Figura 2. Formulario Crear rol del sistema.</figcaption></figure>

<ol class="pasos">
<li>Entre a <strong>Roles del sistema</strong> y pulse <strong>Nuevo rol</strong>.</li>
<li>Complete <strong>Código interno</strong>, <strong>Nombre visible</strong> y elija el <strong>Panel</strong>.</li>
<li>Si el panel es <strong>Hospitalario</strong>, elija el <strong>Tipo de cuenta hospitalaria</strong>.</li>
<li>Marque los <strong>Módulos permitidos</strong> (y, si lo desea, solo algunos submódulos).</li>
<li>Marque, si corresponde, los <strong>Grupos ocupacionales permitidos</strong> y los <strong>Permisos de acción</strong>.</li>
<li>Pulse <strong>Crear Rol</strong>.</li>
</ol>

| Campo | Obligatorio | Descripción |
|---|:-:|---|
| Código interno | <span class="si">Sí</span> | Identificador técnico. Use MAYÚSCULAS con guion bajo, por ejemplo `SUPERVISOR_RRHH`. Si falta: *El codigo interno es requerido*. |
| Nombre visible | <span class="si">Sí</span> | Nombre que verán los administradores. Si falta: *El nombre visible es requerido*. |
| Panel | <span class="si">Sí</span> | **SIGARH** o **Hospitalario**. Al cambiarlo se limpian los módulos, el módulo requerido y los permisos de acción. |
| Tipo de cuenta hospitalaria | Solo panel Hospitalario | Médico, Enfermería, Administrativo, Farmacéutico, Laboratorista, Cajero, Imagenólogo o Archivo clínico. Al cambiarlo se limpian los módulos y los grupos ocupacionales. |
| Módulo requerido | <span class="no">No</span> | Módulo sin el cual el rol no funciona. Debe estar incluido entre los permitidos. |
| Descripción | <span class="no">No</span> | Alcance y responsabilidades del rol. |
| Módulos permitidos | — | Árbol de módulos y submódulos (3.3). |
| Grupos ocupacionales permitidos | <span class="no">No</span> | Si queda vacío, **no hay restricción por grupo**. |
| Permisos de acción | Solo panel SIGARH | Ver 3.4. |
| Alcance global | — | Ver 3.5. |
| Rol activo | — | Activado por defecto. |

## 3.3 Módulos y submódulos permitidos

El árbol muestra los módulos del panel elegido. Cada módulo tiene una casilla:

- **Casilla completa**: el rol da acceso a **todos** los submódulos del módulo.
- **Casilla parcial** (guion): solo algunos submódulos. Pulse la flecha del módulo para desplegarlos y marque los que correspondan; junto al módulo se ve cuántos hay marcados, por ejemplo *3/7*.
- **Seleccionar todos / Quitar todos** marca o limpia el árbol completo.

El sistema solo acepta módulos que el hospital tenga activos en el ERP. Si marca todos los submódulos de un módulo, el sistema lo convierte en el módulo completo.

!!! note "Nota"
    En el panel Hospitalario, algunos submódulos muestran la etiqueta **Aún no restringe**: son solo de referencia y hoy el acceso real sigue siendo a nivel de módulo completo. Los que no tienen la etiqueta (Consulta Externa y Seguimiento de hospitalizados) sí limitan de verdad.

## 3.4 Permisos de acción (panel SIGARH)

Un rol puede ver un módulo sin poder realizar ciertas acciones. Estos permisos habilitan las acciones concretas:

| Permiso | Habilita | Requiere el módulo |
|---|---|---|
| **Aprobar roles de turno** | Aprobar los roles de turno. | Roles Pendientes |
| **Administrar Mantenimiento** | Crear y editar los catálogos de Mantenimiento. | Mantenimiento |
| **Administrar Seguridad** | Crear, editar y desactivar usuarios, perfiles y roles; sin esto solo puede verlos. | Mantenimiento |

Si marca un permiso sin su módulo, el sistema lo rechaza: *Administrar requiere el módulo Mantenimiento* o *Aprobar turnos requiere el módulo Roles Pendientes*. Los roles del panel Hospitalario **no admiten** permisos de acción de SIGARH.

## 3.5 Alcance global

- **Apagado** (valor por defecto): un permiso como *Aprobar roles de turno* solo se aplica al empleado marcado como **jefe del servicio** del rol.
- **Encendido**: el permiso se aplica a todos los servicios.

## 3.6 Editar un rol

Haga clic en el rol o elija **Editar**. Se aplican reglas de protección:

| Regla | Mensaje del sistema |
|---|---|
| Un rol **en uso** no puede cambiar de panel ni de tipo de cuenta. | *No cambie el panel o tipo de cuenta de un rol utilizado; cree otro rol* |
| No se pueden otorgar permisos o alcance global que usted no tenga. | *No puede otorgar permisos que usted mismo no tiene* / *No puede otorgar alcance global sin tenerlo usted mismo* |
| No puede modificar las autorizaciones del rol que usted mismo usa (activo, módulos, permisos, alcance). | *Otra persona administradora debe modificar sus propias autorizaciones* |
| Los módulos elegidos deben estar habilitados en el hospital. | *Los módulos deben existir y estar habilitados para SIGARH en este hospital* |

!!! important "Importante"
    Los cambios en un rol afectan a los perfiles que lo usan, y por tanto a todas las cuentas que dependen de ellos. Revise antes de guardar. Conviene crear pocos roles, amplios y bien nombrados, y afinar el acceso de cada equipo con los perfiles.
