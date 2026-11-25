# 2. Crear un rol

Ruta: **Creación de Roles › (categoría) › (tipo de rol)**. Si la categoría tiene un solo tipo de rol (Residentes, Internos), entra directamente a su lista; si tiene varios, primero elige el tipo en unas tarjetas con su descripción.

Los tipos de rol son: **Ordinario** (jornada ordinaria del mes con actividades y turnos), **Horas Complementarias** (fuera de la jornada ordinaria), **Retén** (disponibilidad para emergencias), **Ordinario sin Actividad** (sin detalle de actividades), **Ordinario con Actividad** y **Horas Complementarias con Actividad** (detallados por actividad) y **Rol de Turnos** (turnos rotativos del internado).

## 2.1 La lista de roles

<figure class="captura"><div class="marco"><img src="img/roles-lista.png" alt="Lista de roles en trabajo de una modalidad" data-ruta="/sigarh/creacion-roles/medicos/ordinario" data-perfil="Elaborador de roles (datos de prueba)"></div>
<figcaption>Figura 1. Lista de roles de una modalidad.</figcaption></figure>

- **Indicadores:** Roles en trabajo, Borradores, Rechazados por corregir y Personal programado. Pestañas **Todos**, **Borradores** y **Rechazados**.
- **Búsqueda:** *Buscar por servicio o departamento*.
- **Tabla:** Servicio, Período, Personal, Actividades y Estado. Si un rol fue rechazado, al pasar el cursor sobre su estado se ve el **motivo del rechazo**.
- **Acciones:** **Abrir y programar** y **Eliminar** (solo roles en borrador o rechazados: *Solo se pueden eliminar roles en borrador o rechazados*).

## 2.2 Datos generales del rol

Pulse **Nuevo rol**. La pantalla define *el ámbito y el período de la programación*.

<figure class="captura"><div class="marco"><img src="img/roles-nuevo.png" alt="Formulario Nuevo rol" data-ruta="/sigarh/creacion-roles/medicos/ordinario/create" data-perfil="Elaborador de roles (datos de prueba)"></div>
<figcaption>Figura 2. Datos generales del rol.</figcaption></figure>

<ol class="pasos">
<li>Elija el <strong>Departamento</strong>. Al cambiarlo se limpia el servicio.</li>
<li>Elija el <strong>Servicio</strong>. Solo se ofrecen los del departamento. Este dato determina qué personal se ofrece para agregar.</li>
<li>Elija el <strong>Mes de cobertura</strong> y el <strong>Año</strong> (con los botones <strong>–</strong> y <strong>+</strong>).</li>
<li>Pulse <strong>Crear y continuar</strong>. El rol se crea como <strong>Borrador</strong> y se abre su editor.</li>
</ol>

| Campo | Obligatorio | Descripción |
|---|:-:|---|
| Departamento | <span class="si">Sí</span> | *El departamento es requerido*. Debe estar activo. |
| Servicio | <span class="si">Sí</span> | *El servicio es requerido*. Debe pertenecer al departamento. |
| Mes de cobertura | <span class="si">Sí</span> | Mes que se programa. |
| Año | <span class="si">Sí</span> | Por defecto, el año actual. |

!!! important "Importante"
    **En el Rol Ordinario de Médicos no puede haber más de un rol por departamento, servicio y período**: *Ya existe un rol médico ordinario para ese departamento, servicio y período.* Abra el existente desde la lista en lugar de crear otro.

Si faltan departamentos o servicios, la pantalla avisa *Falta configurar la estructura asistencial* y deshabilita el botón de crear.
